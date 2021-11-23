import os
from flask import Flask



'''
create_app 是一个应用工厂函数，后面的教程中会用到。这个看似简单的函数其实已经做了许多事情。

app = Flask(name, instance_relative_config=True) 创建Flask 实例。
name 是当前 Python 模块的名称。应用需要知道在哪里设置路径，使用 name 是一个方便的方法。
instance_relative_config=True 告诉应用配置文件是相对于instance folder 的相对路径。实例文件夹在flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统。

app.config.from_mapping() 设置一个应用的缺省配置：
SECRET_KEY 是被 Flask 和扩展用于保证数据安全的。在开发过程中，为了方便可以设置为 'dev' ，但是在发布的时候应当使用一个随机值来重载它。
DATABASE SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的app.instance_path 之内。下一节会更详细地学习数据库的东西。

app.config.from_pyfile() 使用config.py 中的值来重载缺省配置，如果 config.py 存在的话。例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现测试和开发的配置分离，相互独立。
os.makedirs() 可以确保app.instance_path 存在。 Flask 不会自动创建实例文件夹，但是必须确保创建这个文件夹，因为 SQLite 数据库文件会被保存在里面。

@app.route() 创建一个简单的路由，这样在继续教程下面的内容前你可以先看看应用如何运行的。它创建了 URL /hello 和一个函数之间的关联。这个函数会返回一个响应，即一个 'Hello, World!' 字符串。
'''

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'MYBLOG.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    import db
    db.init_app(app)

    # 注册分组路由，即flask的蓝图
    import auth
    app.register_blueprint(auth.bp)

    import blog
    app.register_blueprint(blog.bp)

    import user
    app.register_blueprint(user.bp)


    return app
