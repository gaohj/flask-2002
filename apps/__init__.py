from flask import Flask
from .views import config_blueprint

#封装一个函数 专门用来创建app
#开发过程中 有 生产环境、测试环境、开发环境
#需要三个数据库 为了提升效率 传参数 指定你的环境是哪一个
def create_app():
    app = Flask(__name__)
    #配置蓝本
    config_blueprint(app)
    return app