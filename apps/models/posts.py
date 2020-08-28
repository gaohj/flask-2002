from apps.exts import db
from datetime import datetime

# id   rid
# 1    0
# 2    0
# 3     0
# 4     1
# 5     1
# 6     1
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    rid = db.Column(db.Integer,index=True,default=0)
    content = db.Column(db.Text)
    pub_time = db.Column(db.DateTime,default=datetime.utcnow)

    uid = db.Column(db.Integer,db.ForeignKey("users.id"))
    author = db.relationship("User",backref="postes")

    def __repr__(self):
        return 'Posts:id:%d' % self.id
