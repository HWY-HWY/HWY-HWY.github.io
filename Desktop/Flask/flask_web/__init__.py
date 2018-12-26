# -*- coding: utf-8 -*-
# @File  : __init__.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 创建一个方法创建app，并且执行响应的初始化

from flask import Flask


def create_app():
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object("config")
    # 调用蓝图注册函数，将蓝图与app相关联
    register_blueprint(app)
    return app


def register_blueprint(app):
    from flask_web.blueprint1.views import blueprint
    from flask_web.blueprint2.views.views import blueprint2
    # 注册蓝图对象, 从而就将app与蓝图关联起来了
    app.register_blueprint(blueprint)
    app.register_blueprint(blueprint2)

