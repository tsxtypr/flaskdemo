import os
# 根目录的绝对路径
BASE_DIR=os.path.abspath(os.path.dirname(__file__))
# print(BASE_DIR)
STATIC_PATH=os.path.join(BASE_DIR,'static')

class Config:
    # 正式环境的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost/flask'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  ## 请求结束后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True  ### 跟踪修改 flask1.x版本之后的配置项
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SESSION_TYPE='filesystem'
    SECRET_KEY = "ertdesytcut5wsyttiersftudtriuyft=="
    DEBUG = True

class TestConfig:
    # 测试环境的配置
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'test.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 请求结束后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True  # 跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 消除警告
    SECRET_KEY="greagaeofjoewapfde"
    DEBUG = True


