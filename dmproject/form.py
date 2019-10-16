import wtforms
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import ValidationError

## 自定义校验
def keywords_valid(form,field):
    """
    判断是否包含敏感字段
    不需要手动传参
    :param form:
    :param field:
    :return:
    """
    data = field.data
    keywords = ['admin','管理员','香港']
    if data in keywords:
        raise ValidationError('不可以是敏感词汇')
class TaskForm(FlaskForm):
    name = wtforms.StringField(
        render_kw={
        'class':'form-control',
        'placeholder':'任务名'
    },
        validators=[
            validators.DataRequired('任务的名字不能为空'),
            keywords_valid
        ]
    )
    description = wtforms.TextField(
        render_kw={
        'class':'form-control',
        'placeholder':'任务描述'
    }
    )
    time = wtforms.DateField(render_kw={
        'class':'form-control',
        'placeholder':'创建时间'
    })
    public = wtforms.StringField(render_kw={
        'class':'form-control',
        'placeholder':'发布人'
    })