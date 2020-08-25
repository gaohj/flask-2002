from flask import Blueprint,render_template,redirect,url_for
from apps.models import User
from apps.forms import RegisterForm
from apps.exts import db
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
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)