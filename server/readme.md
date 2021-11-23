* Windows vscode的启动说明
1. 激活虚拟环境
```shell
.\blog_venv\Scripts\activate
```

2. 安装flask
```shell
pip install Flask
```

3. 导出应用

```shell
$env:FLASK_APP = "./src/init.py"
```

4. 设置运行模式

```shell
$env:FLASK_ENV = "development"  
```

5. 运行

```shell
flask run
```

6. 如果需要初始化数据库

```shell
flask init-db
```


7. 如需退出虚拟环境

```shell
deactivate
```

8. 创建虚拟环境

```shell
python -m venv <name>
```

# 技术栈
* 前端



* 后端

flask 
sqlite


