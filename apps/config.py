
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)
#通用配置
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ADADSF1212'
    #bootstrap使用本地的静态文件
    BOOTSTRAP_SERVE_LOCAL = True
    PAGE_COUNT = 10
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'gaohj5@163.com'
    MAIL_PASSWORD = 'TLNOFJSYQPYWISOA'

    #上传文件的设置
    MAX_CONTENT_LENGTH = 1024*1024*8

    #上传位置设置
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir,'static/uploads')



#开发环境
class DevelopmentConfig(Config):
    # 数据库的配置变量
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'kangbazi2002'
    USERNAME = 'root'
    PASSWORD = '123abc'
    # 用户名:密码@数据库地址:端口号/数据库名字
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'testing.sqlite')

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'product.sqlite')

config = {
    'test':TestingConfig,
    'product':ProductionConfig,
    'default':DevelopmentConfig,
}
