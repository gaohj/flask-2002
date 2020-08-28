from exts import db

#用户表
#文章表
#标签表

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50),unique=True)

article_tag_table = db.Table('article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True),

)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship("User",backref='articles')

    tags = db.relationship('Tag',secondary=article_tag_table,backref='tags')

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),unique=True)