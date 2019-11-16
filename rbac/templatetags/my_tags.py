#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: my_tags.py

@time: 2019-11-16 22:20

@desc:

'''

from django import template

register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def get_menu(request, ):
    # 获取放到菜单中的权限
    menu_permission_list = request.session["menu_permission_list"]
    return {"menu_permission_list": menu_permission_list}
