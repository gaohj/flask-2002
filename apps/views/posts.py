from flask import Blueprint,render_template,jsonify
from .decorators import login_requireds
from flask_login import current_user


posts = Blueprint("posts",__name__)


# 用来处理收藏和取消收藏
@posts.route('/collect/<pid>/')
# @login_requireds
def collect(pid):
    #原来收藏  点击 变成 取消收藏
    if current_user.is_favorite(pid):
        current_user.del_favorite(pid)
    else:
        current_user.add_favorite(pid)
    return jsonify({'result':'ok'})
    #异步操作   #多件事情 一起做
    #点击收藏
    #收藏

    #没收藏    点击 收藏

    # 用户  收藏

    # 用户 取消收藏

    # 判断是否收藏