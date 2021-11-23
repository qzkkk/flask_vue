from flask import (
    Blueprint, request,  jsonify
)

import auth
import db as mydb

bp = Blueprint('blog', __name__, url_prefix="/blogs")

# login_required = auth.login_required


@bp.route('/', methods=['GET'])
def index():
    db = mydb.get_db()
    posts = db.execute(
        '''
        SELECT p.id, title, body, created, author_id, username
         FROM post p JOIN user u ON p.author_id = u.id
         ORDER BY created DESC
        '''
   
    ).fetchall()
    ret = [dict(p) for p in list(posts)] 

    # 注意这里把datetime转成字符串
    return  jsonify(ret),200
    
# 创建文章
@bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        data = []
    title = data['title'] if 'title' in data else None
    body = data['body'] if 'body' in data else "默认内容"
    error = None
    if not title:
        return jsonify({
            "result": "title is required."
        }), 400
    else:
        db = mydb.get_db()
        db.execute(
            'INSERT INTO post (title, body, author_id)'
            ' VALUES (?, ?, ?)',
            (title, body, g.user['id'])
        )
        db.commit()
        return jsonify({
            "result": f'{title} create successfully'
        }), 201
    
# 删除文章
@bp.route('/<int:id>', methods=('DELETE',))
# @login_required
def delete(id):
    db = mydb.get_db()
    ret = db.execute('SELECT *  FROM post WHERE id = ?', (id,)).fetchone()
    if ret is None:
        return jsonify({
            "result": f'{id} is not existed'
        }), 400

    ret = dict(ret)
    print(ret)
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return jsonify({
        "result":f"{id} is deleted"
    })


# 根据文章id更新文章信息
@bp.route('/<int:id>', methods=['PUT'])
# @login_required
def update(id):
    db = mydb.get_db()
    post =  db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    # 将数据库数据结果转换成为字典
    post = dict(post)
    # print(post['body'])
    data = request.get_json()
    title = data['title'] if 'title' in data else post['title']
    body = data['body'] if 'body' in data else post['body']
    
    db.execute(
        'UPDATE post SET title = ?, body = ?'
        ' WHERE id = ?',
        (title, body, id)
    )
    ret = db.execute(
        'SELECT * FROM post WHERE post.id = ?',(post['id'],)
    ).fetchone()
    db.commit()
    ret = dict(ret)
    return jsonify(ret)

# 根据文章id获取文章信息
@bp.route('/<int:id>',methods=('GET',))
def get_post(id):
    post = mydb.get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    if post is None:
        return jsonify({
            "result":f"blog {id} is not existed"
        }), 400
    post = dict(post)
    return jsonify(post)




