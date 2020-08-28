HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_restful_demo'
USERNAME = 'root'
PASSWORD = '123456'
# 用户名:密码@数据库地址:端口号/数据库名字
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False