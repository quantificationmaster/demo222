from flask import Flask,render_template,request,session,redirect
from flask import url_for
import functools
import pymysql
import config
from exts import db
from flask_migrate import Migrate
from model import Teacher,CourseTeacher,Course



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

migrate=Migrate(app,db)

@app.route('/')
def hello_world():
    s=Teacher.query.filter_by(name='xx').first()
    print(s.teacher_courses[0].name)
    # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
