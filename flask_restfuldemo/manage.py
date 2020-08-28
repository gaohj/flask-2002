from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from app import app
from models import User,Article,Tag

manager = Manager(app)
Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.command
def add_data():
    user = User(username='张三',email='zhangsan@gmail.com')
    article  = Article(title='钢铁是怎样炼成的',content='没有金刚钻就不揽瓷器活')
    article.author = user
    tag1 = Tag(name='人物传记')
    tag2 = Tag(name='故事会')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    print('添加数据成功')
if __name__ == '__main__':
    manager.run()