from flask import Flask
from .views import config_blueprint
from .exts import config_extensions
from .config import config
#封装一个函数 专门用来创建app
#开发过程中 有 生产环境、测试环境、开发环境
#需要三个数据库 为了提升效率 传参数 指定你的环境是哪一个
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #配置蓝本
    config_blueprint(app)
    config_extensions(app)
    return app