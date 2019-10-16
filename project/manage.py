from main import app,db
import sys
from views import *
from models import *
from flask_script import Manager

# runserver
manager=Manager(app)

# 数据迁移
@manager.command
def migrate():
    db.create_all()

if __name__ == '__main__':
    manager.run()


# command=sys.argv
# print(command)
#
#
# # if command[1]=='runserver' and command[2]=='0.0.0.0:8000':
# #     app.run(host='0.0.0.0',port=8000)
# if command[1]=='runserver':
#     app.run()
# elif command[1]=='migrate':
#     db.create_all()

