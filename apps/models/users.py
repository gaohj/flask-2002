from apps.exts import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(64),unique=True)
    #是否激活
    confirmed = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(128),default='default.jpg')