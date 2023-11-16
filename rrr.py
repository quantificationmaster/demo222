from exts import db
from flask import Blueprint, render_template, request
from models import *
from sqlalchemy import  text
from flask import session, redirect
from flask import jsonify
r1 = Blueprint("rrr", __name__, url_prefix='/')

def cun(id):
    query = text('select * from User where username="{}"'.format(id))
    results = db.session.execute(query).fetchone()
    if results==None:
        return 0
    else:
        return 1
@r1.route('/reg',methods=['POST'])
def reg():
    data = request.get_json()
    username = data['username']
    password = data['password']
    type=data['type']
    index=data['index']
    if cun(username)==1:
        k1=User(type=type,username=username,password=password)
        db.session.add(k1)
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': '用户名已存在'})


