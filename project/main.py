from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)


BASE_DIR=os.path.abspath(os.path.dirname(__file__)) #当前文件  项目的根目录
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123@localhost/flask"
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True  #请求结束后自动提交
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"]=True #跟踪修改
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True #消除警告
# app.config['DEBUG']=True

app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config")
app.secret_key='falfjlkdsflkdasc'
# app.config.from_envvar()  #从环境变量中加载
# app.config.from_json()  #从json串中加载
# app.config.from_mapping()   #字典类型
db=SQLAlchemy(app)






