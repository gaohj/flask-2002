from flask import Blueprint,render_template,redirect,url_for,flash
from apps.models import User
from apps.forms import RegisterForm,LoginForm
from apps.exts import db
from apps.email import send_mail
from flask_login import login_user,logout_user
users = Blueprint("users",__name__)



@users.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('该用户名不存在')
        elif not u.confirmed:
            flash('该用户还没激活')
        elif u.verify_password(form.password.data):
            login_user(u,remember=form.remember.data)
            flash('登录成功')
            return redirect(url_for('main.index'))
        else:
            flash('无效的密码')
    return render_template('users/login.html',form=form)
@users.route('/logout/')
def logout_demo():
    logout_user()
    flash('退出登录成功')
    return redirect(url_for('main.index'))


@users.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate():
        u = User(username= form.username.data,password = form.password.data,
        email = form.email.data)
        db.session.add(u)
        db.session.commit()

        #生成一个加密的字符串 保存该用户注册成功后的信息
        token = u.generate_token()
        #发送给用户一封邮件
        send_mail(u.email,'77账户激活','email/activate',username=u.username,token=token)
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)

#当用户点击链接 然后这个方法响应
@users.route('/activate/<token>/')
def activate_user(token):
    if User.check_activate_token(token):
        flash('账户已经激活')
        return redirect(url_for('users.login'))
    else:
        flash('账户激活失败')
        return redirect(url_for('main.index'))