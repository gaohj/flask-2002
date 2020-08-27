from flask import Flask,request,views,render_template

app = Flask(__name__)


@app.route('/',methods=['GET','POST','PUT','DELETE','PATCH'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World get!'
    elif request.method == 'POST':
        return 'Hello World post!'
    elif request.method == 'PATCH':
        return 'Hello World PATCH!'
    elif request.method == 'DELETE':
        return 'Hello World DELETE!'
    else:
        return 'hello'

class TestView(views.View):
    def __init__(self):
        super(TestView, self).__init__()
        self.context = {
            'name':'千锋教育',
            'phone':'13888888888'
        }
class DoubanView(TestView):
    #每个子类必须有dispatch_request方法
    def dispatch_request(self):
        return render_template('douban.html',**self.context)


class ZhihuView(TestView):
    def dispatch_request(self):
        return render_template('zhihu.html',**self.context)


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')
    def post(self):
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        return 'success'


class ApiView(views.MethodView):
    def get(self):
        return 'get'
    def post(self):
        return 'post'
    def put(self):
        return 'put'
    def patch(self):
        return 'patch'
    def delete(self):
        return 'delete'
app.add_url_rule('/douban/',view_func=DoubanView.as_view('doubanview'))
app.add_url_rule('/zhihu/',view_func=ZhihuView.as_view('zhihuview'))
app.add_url_rule('/login/',view_func=LoginView.as_view('loginview'))
app.add_url_rule('/api/',view_func=ApiView.as_view('apiview'))
if __name__ == '__main__':
    app.run(debug=True)
