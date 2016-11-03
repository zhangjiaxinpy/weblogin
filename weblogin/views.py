# coding:utf-8
from django.shortcuts import *
from django.http import *
from models import *
import hashlib
from django.contrib.sessions.models import *
from . import decorate


# Create your views here.
# @decorate.loginYz
@decorate.loginName
def indexHtml(request, dic, *args):
    """
    主页面渲染
    :param request:
    :return:
    """
    # request.session['username'] = 'ppppp'
    return render_to_response('weblogin/index.html', dic)


def registerHtml(request):
    """
    渲染注册页面
    :param request:
    :return:
    """
    return render(request, 'weblogin/register.html')


def registerHandler(request):
    """
    注册执行
    :param request:
    :return:
    """
    if request.method == 'POST':
        uName = request.POST['user_name']
        uPwd = request.POST['pwd']
        eMail = request.POST['email']
        # 对密码进行md5加密
        encrypt = hashlib.md5()
        encrypt.update(uPwd)
        # isEmpty = UserInfo.objects.get(uName=uName)
        # 在数据库中查找是否用户名已存在
        try:
            UserInfo.objects.get(uName=uName)
        except Exception:
            UserInfo.objects.create(uName=uName, uPwd=encrypt.hexdigest(), uEmail=eMail)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect("用户名存在了")


def loginHtml(request):
    """
    登录页面渲染
    :param request:
    :return:
    """
    return render(request, 'weblogin/login.html')


def loginHandler(request):
    """
    登录操作执行验证
    :param request:
    :return:
    """
    if request.method == 'POST':
        uName = request.POST['username']
        uPwd = request.POST['pwd']
        # uReb = request.POST['reb']
        encrypt = hashlib.md5()
        encrypt.update(uPwd)
        user = UserInfo.objects.filter(uName__exact=uName, uPwd__exact=encrypt.hexdigest())
        if user:
            # 比较成功，跳转index
            # user = UserInfo.objects.get(uName=uName)
            request.session['username'] = uName
            response = redirect('/index/')
            # response = render_to_response('weblogin/index.html', {'user': user})

            # response.set_cookie('username', uName, 3600)
            return response
        else:
            return HttpResponseRedirect('/login/')


# def loginSucceed(request):
#     """
#     登录成功
#     :param request:
#     :return:
#     """
#     # userName = request.COOKIES.get('username')
#     userName = request.session.get('username')
#     response = render_to_response('weblogin/baseBottom.html', {'user': userName})
#     return response


def loginOut(request):
    """
    退出登录
    :param request:
    :return:
    """
    response = HttpResponseRedirect('/index/')
    # response.delete_cookie('username')
    del request.session['username']
    return response


@decorate.loginYz
@decorate.loginName
def cart(request, dic):
    return render(request, 'weblogin/cart.html', dic)
