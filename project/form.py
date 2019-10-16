from flask_wtf import FlaskForm
import wtforms
from wtforms import validators,ValidationError


# 自定义校验
def keywords_valid(form,field):
    """

    :param form:表单
    :param field: 字段
    :return:
    """
    data=field.data
    keywords=['admin','管理员','香港']
    if data in keywords:
        raise ValidationError("不可以是敏感词")

class TaskForm(FlaskForm):
    # 属性
    name=wtforms.StringField(label="任务名字")
    description=wtforms.TextField(label="任务描述")
    time=wtforms.DateField(label="任务时间")
    public=wtforms.StringField(label="任务发布人")
