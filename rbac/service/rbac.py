#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: rbac.py

@time: 2019-11-15 14:48

@desc:

'''

import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class ValidPermission(MiddlewareMixin):

    def process_request(self, request):
        # 当前路径
        current_path = request.path_info
        print('currentpath', current_path)
        # 白名单
        varlid_url_list = ["/login/", "/reg/", "/admin/.*"]
        for valid_url in varlid_url_list:
            ret = re.match(valid_url, current_path)
            if ret:
                return None

        # 检验是否登录,未登录跳转到登录页面
        user_id = request.session.get('user_id')
        print(user_id)
        if not user_id:
            return redirect('/login/')

        # 权限校验
        permission_dict = request.session.get('permissions_dict')

        # 如果获取的权限列表为空，则为重新定位到登录页面
        # print('1222',permission_dict.values())
        if not permission_dict:
            return redirect('/login/')

        for item in permission_dict.values():
            urls = item['urls']
            for reg in urls:
                reg = "^%s$" % reg
                ret = re.match(reg, current_path)
                if ret:
                    print('actions', item['actions'])
                    request.actions = item['actions']
                    return None

        return HttpResponse('没有访问权限！！！！')
