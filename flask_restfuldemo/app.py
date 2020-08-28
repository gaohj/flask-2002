from flask import Flask,views,url_for
# from flask_restful import Api,Resource,reqparse,inputs,marshal_with,fields
from article_view import article_bp
from exts import db
import config
app = Flask(__name__)
# api = Api(app)
app.config.from_object(config) #让配置文件生效
app.register_blueprint(article_bp,url_prefix='/article') #注册蓝本
db.init_app(app) #扩展实例化

@app.route('/')
def hello_world():
    print(url_for('hello_world'))
    print(url_for('myview'))
    print(url_for('users'))
    return 'Hello World!'

class TestView(views.MethodView):
    def get(self):
        print('get')
        return 'get'
    def post(self):
        return 'post'

app.add_url_rule('/test/',view_func=TestView.as_view('myview'))


# class UsersView(Resource):
#     def get(self):
#         return {"username":"kangbazi"}
#     def post(self):
#         from datetime import date
#         print(date)
#         parser = reqparse.RequestParser() #实例化一个parser对象
#         parser.add_argument('username',type=str,help="用户名输入错误",trim=True,required=True)
#         parser.add_argument('password',type=str,help="密码输入错误")
#         parser.add_argument('age',type=int,help="年龄必须符合要求")
#         parser.add_argument('gender',type=str,choices=['male','female','secret'])
#         parser.add_argument('telephone',type=inputs.regex(r'^1[3456789]\d{9}$'))
#         parser.add_argument('homepage',type=inputs.url,help='请输入正确的url地址')
#         parser.add_argument('birth',type=inputs.date,help='生日字段验证错误')
#
#         args = parser.parse_args()
#         return {"password":"asdfadsfdasfadsfdasfasf"}
# api.add_resource(UsersView,'/users/','/hahahahahaha/',endpoint='users')


# class Article(object):
#     def __init__(self,content,username,age):
#         self.content = content
#         self.username = username
#         self.age = age
#
# article = Article(content='生吃牛肉不用切',username='一天三次',age=18)
#
# class ArticleView(Resource):
#     resource_fields = {
#         'title':fields.String,  #上面没有title字段  这里规定返回  会返回null
#         'username':fields.String,
#         'content':fields.String,
#         'age':fields.Integer,
#     }
#     #
#     @marshal_with(resource_fields)
#     def get(self):
#         return article
#
#
# api.add_resource(ArticleView,'/articles/',endpoint='articles')

if __name__ == '__main__':
    app.run(debug=True)
