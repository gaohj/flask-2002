#导入类库

from flask_bootstrap import Bootstrap



#实例化对象

bootstrap = Bootstrap()


#封装函数 完成初始化

def config_extensions(app):
    bootstrap.init_app(app)