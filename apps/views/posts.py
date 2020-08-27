from flask import Blueprint,render_template
from .decorators import login_requireds

posts = Blueprint("posts",__name__)



@posts.route('/posts/')
@login_requireds
def index():
    return '感谢老铁收藏'