from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app,abort
from apps.models import Posts
from apps.forms import PostsForm
from flask_login import login_required,current_user
from apps.exts import db
main = Blueprint("main",__name__)



@main.route('/',methods=['GET','POST'])
# @login_required
def index():
    form = PostsForm()
    if form.validate():
        #判断是否登录了
        if current_user.is_authenticated:
            #获取当前登录的用户
            u = current_user._get_current_object()
            p = Posts(content=form.content.data,author=u)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('登录以后才可以发表')
            return redirect(url_for('users.login'))

    #读取所有的博客
    # posts = Posts.query.filter_by(rid=0).all()
    # return render_template('main/index.html',form=form,posts=posts)
    #接收用户想查看第几页
    #http://www.baidu.com/?p=1 如果不写p参数 默认为1 类型必须是int 类型
    page = request.args.get('p',1,type=int)
    #拿到分页对象
    pagination = Posts.query.filter_by(rid=0).order_by(Posts.pub_time.desc()).paginate(page,per_page=current_app.config['PAGE_COUNT'],error_out=False)
    posts = pagination.items
    return render_template('main/index.html',form=form,posts=posts,pagination=pagination)

@main.route('/detail/<postid>/')
def post_detail(postid):
    post = Posts.query.get(postid)
    if not post:  #如果没有帖子详情 那么我们就抛出404错误
        abort(404)

    #查询帖子的评论内容
    comments = Posts.query.filter_by(rid=postid).order_by(Posts.pub_time.desc()).all()
    return render_template('main/detail.html',post=post,comments=comments)