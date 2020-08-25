from flask import Blueprint,render_template,redirect,url_for,flash
from apps.models import User
from apps.forms import RegisterForm
from apps.exts import db
from apps.email import send_mail
users = Blueprint("users",__name__)



@users.route('/login/')
def login():
    return render_template('users/login.html')


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

@users.route('/activate/<token>/')
def activate_user(token):
    if User.check_activate_token(token):
        flash('账户已经激活')
        return redirect(url_for('users.login'))
    else:
        flash('账户激活失败')
        return redirect(url_for('main.index'))