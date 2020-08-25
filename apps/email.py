from flask import current_app,render_template
from apps.exts import mail
from flask_mail import Message
from threading import Thread
def async_send_mail(app,msg):
    with app.app_context():
        mail.send(message=msg)


#封装函数 邮件发送

def send_mail(to,subject,template,**kwargs):
    #获取当前的实例
    app = current_app._get_current_object()
    #message对象
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])

    #浏览器打开显示的内容
    msg.html = render_template(template+'.html',**kwargs)

    #客户端打开
    msg.body = render_template(template+'.txt',**kwargs)

    #创建线程
    thr = Thread(target=async_send_mail,args=[app,msg])

    #启动线程
    thr.start()

    return thr
