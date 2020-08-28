from flask import Blueprint
from flask_restful import Resource,marshal_with,Api,fields
from models import Article
article_bp = Blueprint('article',__name__)

api = Api(article_bp)
class ArticleView(Resource):
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
    }
    @marshal_with(resource_fields) #字典作为参数传给 装饰器  marshal_with
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article
api.add_resource(ArticleView,'/<article_id>/',endpoint='articles')

@article_bp.route('/haha/')
def index():
    return '我是文章首页'