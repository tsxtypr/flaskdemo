from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
from datetime import datetime
pymysql.install_as_MySQLdb()

app=Flask(__name__)

@app.route('/')
def index():
    return "ORM测试"

# 学习sqlalchemy
# 连接数据库
# 类似于settings.py 是配置信息  链接sqllit3配置
# BASE_DIR=os.path.abspath(os.path.dirname(__file__)) #当前文件  项目的根目录
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(BASE_DIR,'test.db')
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True  #请求结束后自动提交
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"]=True #跟踪修改


BASE_DIR=os.path.abspath(os.path.dirname(__file__)) #当前文件  项目的根目录
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123@localhost/flask"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True  #请求结束后自动提交
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"]=True #跟踪修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True #消除警告
app.config['DEBUG']=True

db=SQLAlchemy(app)  #绑定flask项目

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
class PersonalInfo(BaseModel):
    __tablename__='personalinfo'  #指定表名
    # id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32))
    age=db.Column(db.Integer,default=1)
    time=db.Column(db.DATETIME,default=datetime.now())



# 数据迁移
db.create_all()  #同步表结构

# 使用封装的ORM,对数据进行修改
# 增加数据
# user=PersonalInfo(name='zs',age=22)
# user.save()

# 修改数据
# user=PersonalInfo.query.get(3)
# user.name='dm'
# user.merge()

# 删除数据
# user=PersonalInfo.query.get(4)
# user.delete()

# 增加数据
# 增加单条
# personinfo=PersonalInfo(name='zs',age=19)
# db.session.add(personinfo)
# db.session.commit()

# 增加多条
# db.session.add_all([
#     PersonalInfo(name='zs',age=19)
#     PersonalInfo(name='zs',age=19)
#     PersonalInfo(name='zs',age=19)
#     PersonalInfo(name='zs',age=19)
#     PersonalInfo(name='zs',age=19)
# ])
# db.session.commit()
# 查询

# all()返回列表  列表得到每条结果
# data=PersonalInfo.query.all()
# print(data)

# get()  只能传入id  返回一个对象  没有结果返回None
# 不能通过id=1查询！！！！
# data=PersonalInfo.query.get(1)
# data=PersonalInfo.query.get(ident=1)
# print(data)
# print(data.name)

#filter_by  filter
# data=PersonalInfo.query.filter_by(name='zs').all()
# data=PersonalInfo.query(PersonalInfo.name=='zs').all()
# print(data)

# first  返回符合条件的第一条数据  没有数据返回None
# data=PersonalInfo.query.filter_by(name='zs').first()
# print(data)

# order_by
# 按照id升序
# data=PersonalInfo.query.order_by(PersonalInfo.id).all()
# data=PersonalInfo.query.order_by("id").all()
# print(data)
# 按照id降序
# data=PersonalInfo.query.order_by(PersonalInfo.id.desc()).all()
# data=PersonalInfo.query.order_by(db.desc("id")).all()
# print(data)

# 分页
# data=PersonalInfo.query.limit(2).all()
# 跳过几个，选取几个
# data=PersonalInfo.query.offset(2).limit(2).all()
# print(data)

# 修改
# data=PersonalInfo.query.filter(PersonalInfo.id==1).first()
# data.name='lisi'
# db.session.merge(data)
# db.session.commit()

# 删除
# 第一种
# data=PersonalInfo.query.first()
# print(data.id)
# db.session.delete(data)
# db.session.commit()
# 第二种
# data=PersonalInfo.query.filter_by(id=2).delete()
# db.session.commit()

if __name__ == '__main__':
    app.run()