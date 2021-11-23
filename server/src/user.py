from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import db as my_db

bp = Blueprint('user', __name__, url_prefix = '/users')

@bp.route('/', methods=('POST',))
def add_user():
    data = request.get_json()
    username = data['username'] if 'username' in data else None
    password = data['password'] if 'password' in data else None
    db = my_db.get_db()
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
        error = f'username {username} has already existed.'
    if error is None:
        # 这个接口创建的用户默认是管理员
        db.execute(
            'INSERT INTO user (username, password, level) VALUES (?, ?, ?)',
            (username, generate_password_hash(password), 1)
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


@bp.route('/', methods=('DELETE',))
def del_user():
    pass

@bp.route('/', methods=('PUT',))
def update_user():
    pass


# 获取所有用户
@bp.route('/',methods=['GET'])
def get_all_users():
    db = my_db.get_db()
    # 要加鉴权
    users = db.execute(
        'SELECT * FROM user WHERE 1=1'
    ).fetchall()
    # print(f'users=>{users}')
    ret = [dict(user) for user in list(users)]
    return jsonify(ret)

# 获取一个用户的信息
@bp.route('/<int:id>',methods=['GET'])
def get_user_id(id):
    db = my_db.get_db()
    # 要加鉴权
    users = db.execute(
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchall()
    # print(f'users=>{users}')
    ret = [dict(user) for user in list(users)]
    return jsonify(ret)


