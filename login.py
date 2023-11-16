from exts import db
from flask import  Blueprint,render_template,request,jsonify
import json
from models import *
from sqlalchemy import text
from flask import session,redirect
login = Blueprint("login", __name__, url_prefix='/')
def yanzheng(id,pwd):
    query = text('select * from User where username="{}" and password="{}"'.format(id,pwd))
    results = db.session.execute(query).fetchone()
    if results==None:
        return 0
    else:
        return results.type
@login.route('/login',methods=['POST'])
def log():
    data = request.get_json()
    account=data['username']
    password=data['password']
    t = yanzheng(account, password)
    if t == 0:
        return jsonify({'status': 'error', 'message': '用户名或密码错误'})
    else:
        return jsonify({'status': 'success','type':t})



