from flask import Blueprint,render_template


posts = Blueprint("posts",__name__)



@posts.route('/posts/')
def index():
    return '感谢老铁收藏'