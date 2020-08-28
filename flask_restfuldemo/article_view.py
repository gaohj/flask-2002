from flask import Blueprint,g,current_app,jsonify
from flask_restful import Resource,marshal_with,Api,fields
from models import Article
from flask_httpauth import HTTPBasicAuth #导入认证类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
article_bp = Blueprint('article',__name__)

api = Api(article_bp)
auth = HTTPBasicAuth()  #实例化一个认证对象



@auth.verify_password
def verify_password(username_or_token,password):
    #如果传入用户名和密码 然后进行相关的验证
    if username_or_token == 'kangbazi' and password == '123456':
        g.username = username_or_token
        return True

    #当你传过来的是一个token

    s = Serializer(current_app.config['SECRET_KEY'],expires_in=3600) #验证token是否合法
    try:
        data = s.loads(username_or_token)
        g.username = data.get('username')
        return True
    except:
        return False



#这个方法用来获取token
@article_bp.route('/get_token/')
@auth.login_required
def get_token():
    s = Serializer(current_app.config['SECRET_KEY'])
    token = s.dumps({'username':g.username})
    return jsonify({'token':token.decode('utf8')})




class ArticleView(Resource):
    decorators = [auth.login_required]  #给整个类添加装饰器
    resource_fields = {
        'article_title':fields.String(attribute='title'),
        'content':fields.String,
        'author':fields.Nested({  #如果字段下面还有字典  用Nested
            'username':fields.String,
            'email':fields.String,
        }),
        'tags':fields.List(fields.Nested({ #如果字段中放了一个列表  那么用List来表示
            'name':fields.String,   #列表元素是字典  用Nested
        })),
        'counts':fields.Integer(default=100)
    }
    @marshal_with(resource_fields) #字典作为参数传给 装饰器  marshal_with
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article


api.add_resource(ArticleView,'/<article_id>/',endpoint='articles')






@article_bp.route('/haha/')
def index():
    print(g.username)
    return '我是文章首页'