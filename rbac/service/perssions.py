#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: perssions.py

@time: 2019-11-15 13:57

@desc:

'''


# url action 加入到表中去,这个是登陆后调用此方法，内容写入session

def initial_session(user, req):

    # 获取用户所有的权限
    permissions = user.roles.all().values('permissions__url', "permissions__group__id",
                                          "permissions__action").distinct()
    print('permissions', permissions)
    permissions_dict = {}
    for item in permissions:
        gid = item.get('permissions__group__id')
        if not gid in permissions_dict:
            permissions_dict[gid] = {
                "urls": [item["permissions__url"], ],
                'actions': [item["permissions__action"], ]
            }
        else:
            permissions_dict[gid]["urls"].append(item["permissions__url"])
            permissions_dict[gid]["actions"].append(item["permissions__action"])
    print('list', permissions_dict)
    req.session['permissions_dict'] = permissions_dict

    #     注册权限菜单
    permissions_menu = user.roles.all().values('permissions__url', "permissions__action",
                                               "permissions__group__title").distinct()
    print("permissions", permissions_menu)
    menu_permission_list = []
    for item in permissions_menu:
        if item["permissions__action"] == "list":
            menu_permission_list.append((item["permissions__url"], item['permissions__group__title']))
    print(menu_permission_list)
    req.session["menu_permission_list"] = menu_permission_list
