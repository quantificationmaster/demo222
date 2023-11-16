import xlrd
from flask import Blueprint, render_template, session, request, redirect,g
from exts import db
from models import *
from sqlalchemy import text
from flask import url_for
from datetime import datetime
import os,json
from flask import jsonify

tea = Blueprint("teacher", __name__, url_prefix='/')






@tea.route('/teacher/<user>',methods=['POST','GET'])
def teacherq(user):
    if request.method=='GET':
        query = text('select * from teacher2 where teachername="{}"'.format(user))
        results = db.session.execute(query).fetchall()
        result_list = []
        for i in results:
            result_dict = {
                'teachername': i.teachername,
                'lou': i.lou,
                'classroom': i.classroom,
                'timeperiod': i.timeperiod,
                'coursename': i.coursename
            }
            result_list.append(result_dict)
        return jsonify(result_list)



@tea.route('/teacher/<user>/<course>',methods=['GET'])
def stuq(user,course):
    if request.method=='GET':
        query = text('select * from teacherstu where teachername="{}"and coursename="{}"'.format(user,course))
        results = db.session.execute(query).fetchall()
        result_list = []
        for i in results:
            result_dict = {
                'studentname': i.studentname,
                'absence': i.absence
            }
            result_list.append(result_dict)
        return jsonify(result_list)



