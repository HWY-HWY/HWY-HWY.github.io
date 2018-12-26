# -*- coding: utf-8 -*-
# @File  : views1.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 创建另一个视图函数，与views共享一个蓝图

from . import blueprint


@blueprint.route("/index3")
def index3():
    return "共享蓝图"
