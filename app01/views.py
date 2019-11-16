from django.shortcuts import render, HttpResponse

# Create your views here.
from rbac.models import *
from rbac.service.perssions import *


def login(req):
    if req.method == "POST":
        user = req.POST.get('user')
        pwd = req.POST.get('pwd')
        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            req.session['user_id'] = user.pk
            # 调用permissions写入session
            initial_session(user, req)
            return HttpResponse('login sucess ！！！')
    return render(req, 'rbac/login.html')


class Per(object):

    def __init__(self, actions):
        self.actions = actions

    def add(self):
        return "add" in self.actions

    def delete(self):
        return 'delete' in self.actions

    def edit(self):
        return 'edit' in self.actions

    def list(self):
        return 'list' in self.actions


def user(req):
    user_list = User.objects.all()
    id = req.session.get('user_id')
    user = User.objects.filter(id=id).first()
    #
    per = Per(req.actions)
    return render(req, 'rbac/user.html', locals())


def del_user(req, page):
    return HttpResponse('delete !!!!!!')


def roles(req):
    id = req.session.get('user_id')
    user = User.objects.filter(id=id).first()
    role_list = Role.objects.all()
    per = Per(req.actions)
    return render(req, 'rbac/roles.html', locals())


# add role
def add_role(req):
    return HttpResponse('add role')
