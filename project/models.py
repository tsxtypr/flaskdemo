from main import db
from datetime import datetime
class BaseModel(db.Model):
    # 将创建id放在基类中，之后创建模型时，就不用再创建了
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    __abstract__=True   #声明当前类为抽象类，不能重写
    def save(self):
        db.session.add(self)
        db.session.commit()
    def merge(self):
        db.session.merge(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()


# 创建模型
class LoginUser(BaseModel):
    __tablename__='loginuser'
    username=db.Column(db.String(10))
    email=db.Column(db.String(20))
    password=db.Column(db.String(16))
    photo=db.Column(db.String(64),nullable=True)
    # 后加上的
    age=db.Column(db.Integer)
    identity=db.Column(db.String(32))
    study_time=db.Column(db.String(50))
    sex=db.Column(db.String(2))
    phone_number=db.Column(db.String(15))



class Leave(BaseModel):
    __tablename__='leave'
    request_id=db.Column(db.Integer)
    request_name=db.Column(db.String(32))
    request_type=db.Column(db.String(32))  #请假的类型
    request_start=db.Column(db.DATETIME)
    request_end=db.Column(db.DATETIME)
    request_description=db.Column(db.TEXT)  #请假的内容
    request_phone=db.Column(db.String(11))
    # 审核中  0
    # 通过   1
    # 驳回  2
    # 销假  3
    request_status=db.Column(db.Integer)  #请假状态
