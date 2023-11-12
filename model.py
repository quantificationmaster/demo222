from exts import db

#student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))
    stu_no = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    gender=db.Column(db.Enum('男', '女'),nullable=False)
    Absence = db.Column(db.Integer, default=0)
    Absence_t = db.Column(db.Integer, default=0)
    student_course_teachers = db.relationship('Student', secondary='cour_teach_stus')
#grade
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    students = db.relationship('Student', backref='grade')
#classroom
class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    classroom_times = db.relationship('Classroom', secondary='time_classroom')
#course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    course_teachers = db.relationship('Teacher', secondary='course_teacher')
#teacher
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teacher_courses = db.relationship('Course', secondary='course_teacher')
#time
class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    Time_period = db.Column(db.String(20), nullable=False)
    time_classrooms = db.relationship('Time', secondary='time_classroom')
#user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('教师', '督导员','辅导员'),nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

#中间表
#course_teacher
class CourseTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    # course_teacher_students = db.relationship('courseteacher', secondary='cour_teach_stus',)

#time_classroom
class TimeClassroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'))
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))

# 复合中间表
#cour_teach_stus
class cour_teach_stus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    c_t_id=db.Column(db.Integer, db.ForeignKey('course_teacher.id'))
#scheduling
class Scheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t_c_id = db.Column(db.Integer, db.ForeignKey('time_classroom.id'))
    c_t_id=db.Column(db.Integer, db.ForeignKey('course_teacher.id'))