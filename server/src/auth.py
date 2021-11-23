import functools
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
import db as mydb

# Blueprint 是一种组织一组相关视图及其他代码的方式。
bp = Blueprint('auth', __name__, url_prefix='/auth')

# 注册
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username'] if 'username' in data else None
    password = data['password'] if 'password' in data else None

    db = mydb.get_db()
    error = None

    if not username:
        error = 'username is required.'
    elif not password:
        error = 'password is required.'
        
        #  执行sql
    elif db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone() is not None:
    # fetchone 返回一个元组，即一条数据
        error = f'username {username} has already registered.'
    if error is None:
        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()
        result = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        result = dict(result)
        return jsonify(result), 201    
    else:
        result = {
            'result': error
        }
        return jsonify(result), 400
    

# 登录
@bp.route('/login', methods=['POST'] )
def login():
    data = request.get_json()
    username = data['username'] if 'username' in data else None
    password = data['password'] if 'password' in data else None
    
    db = mydb.get_db()
    error = None
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        error = 'Incorrect username.'
    elif password is None:
        error = "Incorrect password"
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'
    if error is None:
        # 登录成功
        session.clear()
        session['user_id'] = user['id']
        user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        user = dict(user)
        user['token'] = "test"
        return jsonify(user), 200
    else:
        return jsonify({
            "result":error
        }), 400




'''
Such a function is executed before each request, even if outside of a blueprint.
'''
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = mydb.get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({
        "result":"logout successfully"
    }) , 200


# def login_required(param):
#     print("=====",param)
#     '''登录权限装饰器'''
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             if g.user is None:
#                 return json.dumps({
#                     "result":"please login"
#                 }), 401
#             else:
#                 return f(*args, **kwargs)
#         return decorated_function
#     return decorator