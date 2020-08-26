from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length


class PostsForm(FlaskForm):
    content = TextAreaField('',render_kw={'placeholder':'这一刻不想说点什么'},validators=[DataRequired(),Length(min=10,max=140,message='说话不要说太多注意分寸')])
    submit = SubmitField('即刻发表')


