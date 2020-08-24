from .main import  main
from .users import users
from .posts import posts

#蓝本的配置  =
DEFAULT_BLUEPRINT = (
    (main,''),
    (users,'/users'),
    (posts,'/posts'),

)

#封装函数 完成蓝本的注册

def config_blueprint(app):
    for blueprint,url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)