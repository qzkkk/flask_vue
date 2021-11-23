[TOC]





---



# 1. 博客搭建的准备工作

## 1.1 技术选型

### 前端

* vue2.x
* vuex
* axios
* antd
* less



### 后端

* python flask
* mysql



# 2. 前端

## 2.1 页面

1. 首页
2. 分类
3. 标签
4. 更新日志
5. 友链
6. 关于我
7. 写博客（进入后台管理页面）





# 3. 后端

## 3.1 restfulAPI设计

> - GET（SELECT）：从服务器取出资源（一项或多项）。
> - POST（CREATE）：在服务器新建一个资源。
> - PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
> - PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
> - DELETE（DELETE）：从服务器删除资源。

| 接口           | 方法 | 参数                         | 功能                         | 备注                       |
| -------------- | ---- | ---------------------------- | ---------------------------- | -------------------------- |
| /login         | post | userName <br/ > pwd          | 登录                         |                            |
| /register      | post | userName<br />phone<br />pwd | 注册                         |                            |
| /info          | get  | /                            | 获取博客的运营时间等相关信息 |                            |
| /index         | get  | /                            | 获取首页的10条最新的文章信息 |                            |
| /articles/:pid | get  | 分页id，默认为1              | 获取分页文章数据             |                            |
| /article/:aid  | get  | 文章id                       | 获取某篇文章的信息           |                            |
| /tags          | get  | /                            | 获取所有的文章标签           |                            |
| /article/:tid  | get  | 标签id                       | 获取某个标签的文章           |                            |
| /categories    | get  | /                            | 获取所有的文章分类           |                            |
| /article/:cid  | get  | /                            | 获取某个分类的文章           |                            |
| /article       | post | /                            | 添加文章                     | 只有给权限的人才可以写博客 |

# api

详情见server的api文件夹

