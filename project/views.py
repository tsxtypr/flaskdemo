from flask import Flask,request
from flask import render_template,redirect
from get_time import GetDate
import hashlib
from models import *
import functools
import os
from settings import STATIC_PATH
from flask import session

app=Flask(__name__)

# 登录装饰器
def LoginValid(func):
    # 使内部函数的名字还是自己的名字
    @functools.wraps(func)
    def inner(*args,**kwargs):
        userid=request.cookies.get("userid")
        email=request.cookies.get('email')
        # session_email=session.get("email")
        # print(session_email)
        if email and userid:
            # 判断是哪个用户
            user=LoginUser.query.filter_by(email=email).first()
            if user:
                return func(*args, **kwargs)
            else:
                return redirect("/login/")
        else:
            return redirect('/login/')
    return inner

# 登录页
@app.route("/index/")
@LoginValid
def index():
    return render_template('index.html')

# 个人中心页
@app.route("/personal_info/")
def personal_info():
    # 获得日程表
    get_date=GetDate()
    dates=get_date.print_date()

    # 获得个人信息
    userid=request.cookies.get("userid")
    personal_info=LoginUser.query.filter_by(id=userid).first()
    return render_template('personal_info.html',**locals())

# 修改个人信息
@app.route('/update_personal/',methods=['get','post'])
def update_personal():
    # 获得个人信息
    userid=request.cookies.get("userid")
    personal_info=LoginUser.query.filter_by(id=userid).first()

    if request.method=="POST":
        data=request.form
        # print(data)
        personal_info.username=data.get("username")
        # 从前端获得到的数据都是字符串
        if data.get("sex")=='0':
            personal_info.sex='男'
        else:
            personal_info.sex = '女'
        personal_info.age=data.get("age")
        if data.get("identity")=='0':
            personal_info.identity='讲师'
        else:
            personal_info.identity = '学生'
        personal_info.phone_number=data.get('phone_number')
        personal_info.study_time=data.get('study_time')
        # 获取图片
        photo=request.files.get("photo")
        # print(photo)
        print(photo)
        if photo:
            photo_name = photo.filename
            photo_path=os.path.join('img',photo_name)
            abspath=os.path.join(STATIC_PATH,photo_path)
            # 这个save是将图片保存在static/img/photoname，这样以后也可以使用
            # print(abspath)
            photo.save(abspath)
            # 数据库中只保存图片的名字   static/photoname
            personal_info.photo=photo_path
        personal_info.merge()


    return render_template('update_personal.html',**locals())


#加密
def setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    res=md5.hexdigest()
    return res

# 登录
@app.route('/login/',methods=['post','get'])
def login():
    error=''
    if request.method=='POST':
        email=request.form.get("email")
        password=request.form.get("password")
        # print(email,password)
        if email and password:
            user=LoginUser.query.filter_by(email=email).first()
            if user:
                check_pwd=LoginUser.query.filter_by(password=setpassword(password)).first()
                if check_pwd:
                    response=redirect("/index/")
                    response.set_cookie('email',email)
                    response.set_cookie('userid',str(user.id))
                    # session['email']=email
                    return response
                else:
                    error='密码不存在'
            else:
                error="该用户不存在"
        else:
            error="不能为空"
    return render_template('login.html')

# 注册
@app.route('/register/',methods=['post','get'])
def register():
    error=''
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        password2=request.form.get('password2')
        # print(username,email,password,password2)
        if username and email and password2 and password:
            user=LoginUser.query.filter(LoginUser.email==email).first()
            if user:
                error = '该用户存在'
            else:
                if password2==password:
                    user=LoginUser(username=username,password=setpassword(password),email=email)
                    user.save()
                    return redirect("/login/")
                else:
                    error='两次密码不一致'
        else:
            error='不能为空'
    return render_template('register.html',**locals())


# 登出
@app.route('/logout/')
def logout():
    response=redirect('/login/')
    response.delete_cookie("email")
    response.delete_cookie("userid")
    return response


# 请假条
@app.route('/leave_list/',methods=['get','post'])
def leave_list():
    if request.method=='POST':
        user_id=request.cookies.get("userid")
        data=request.form

        request_id=int(user_id)
        request_name = data.get("username")
        request_type = data.get("type")  # 请假人的类型
        request_start = data.get("start_time")
        request_end = data.get("end_time")
        request_description = data.get("desc")  # 请假的内容
        request_phone = data.get("phone")
        if data.get("start_time") and data.get("end_time"):
            leave=Leave(request_id=request_id,request_name=request_name,request_type=request_type,
                            request_start=request_start,request_end=request_end,request_description=request_description,request_phone=request_phone,request_status=0)
            leave.save()
    return render_template('leave_list.html')

from flask import jsonify
# 请假条中撤销
@app.route("/redo/",methods=['get','post'])
def redo():
    if request.method=='POST':
        data=request.form
        id=data.get('id')
        print(id)
        leave=Leave.query.filter_by(id=id).first()
        print(leave)
        # leave.delete()
        result={'code':10000,'data':'success'}
    return jsonify(result)

# 请假列表
from sdk.page import Paginator
@app.route('/leave_all_list/<int:page>/',methods=['get','post'])
def leave_all_list(page):
    user_id=request.cookies.get("userid")
    leave_list=Leave.query.filter_by(request_id=user_id)
    # print(leave_list)

    # 进行分页
    paginator=Paginator(leave_list.all(),2)
    # print(paginator)
    page_obj=paginator.page_data(page)
    return render_template('leave_all_list.html',**locals())

# @app.route('/adddata/')
# def adddata():
#     for i in range(100):
#         leave=Leave()

from form import TaskForm
@app.route("/add_task/")
def add_task():
    task=TaskForm()
    error={}
    if request.method=='POST':
        if task.validate_on_submit():
            # 获取数据
            FormData=task.data
    #     保存数据   数据库当中 建立模型
        else:

            error=task.errors
        print(error)
    return render_template('add_task.html',**locals())
if __name__=="__main__":
    app.run(host="0.0.0.0",port="8000",debug=True)