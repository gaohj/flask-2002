from flask import Flask,views
from flask_restful import Api,Resource,reqparse,inputs

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

class TestView(views.MethodView):
    def get(self):
        print('get')
        return 'get'
    def post(self):
        return 'post'

app.add_url_rule('/test/',view_func=TestView.as_view('myview'))


class UsersView(Resource):
    def get(self):
        return {"username":"kangbazi"}
    def post(self):
        from datetime import date
        print(date)
        parser = reqparse.RequestParser() #实例化一个parser对象
        parser.add_argument('username',type=str,help="用户名输入错误",trim=True,required=True)
        parser.add_argument('password',type=str,help="密码输入错误")
        parser.add_argument('age',type=int,help="年龄必须符合要求")
        parser.add_argument('gender',type=str,choices=['male','female','secret'])
        parser.add_argument('telephone',type=inputs.regex(r'^1[3456789]\d{9}$'))
        parser.add_argument('homepage',type=inputs.url,help='请输入正确的url地址')
        parser.add_argument('birth',type=inputs.date,help='生日字段验证错误')

        args = parser.parse_args()
        return {"password":"asdfadsfdasfadsfdasfasf"}
api.add_resource(UsersView,'/users/',endpoint='users')

if __name__ == '__main__':
    app.run(debug=True)
