from flask import session,redirect,url_for
from functools import wraps
from flask_login import current_user
#func是个方法

# @login_required
#def index()
#如果登录了  会执行index方法
# 把index 当作参数传给 login_required
#
def login_requireds(func):
    @wraps(func)
    def inner(*args,**kwargs):
         user = session.get('user_id')
         if user:
            return func(*args,**kwargs)
         else:
             return redirect(url_for('users.login'))
    return inner