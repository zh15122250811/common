import hashlib

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import UserModel


# 首页
def mineIndex(request):
    # 获取user_id
    user_id = request.session.get("user_id")
    res = UserModel.objects.filter(pk=user_id)
    is_login = True

    if not res.exists():
        is_login = False

    user = res.first()
    data = {
        "is_login":is_login,
        "user":user,
    }
    return render(request,"index.html",context=data)

# 请求注册/提交注册
def register(request):
    if request.method == "GET":
        return render(request,"user_register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # 创建对象
        user = UserModel()
        user.username = username
        user.password = create_pass(password)
        user.email = email
        user.save()
        # 设置一个session,注册完成直接返回登录页面
        request.session["user_id"] = user.id
        return redirect(reverse("app:mineindex"))


# 加密
def create_pass(password):
    passsha512 = hashlib.sha512()
    passsha512.update(password.encode("utf-8"))
    return passsha512.hexdigest()


# 验证用户名是否可用
def check_user(request):
    data = {}
    # 获取ajax请求携带的参数 Username
    Username = request.GET.get("Username")
    # 查询数据库
    res = UserModel.objects.filter(username=Username)
    if res.exists():
        data = {
            "code":"901",
            "status":"false",
            "msg":"该用户名已存在,请重新输入"
        }
    else:
        data = {
            "code": "200",
            "status": "true",
            "msg": "该用户名可用",
        }
    return JsonResponse(data)


# 退出操作
def logout(request):
    # 清除session
    request.session.flush()
    return redirect(reverse("app:mineindex"))


# 请求登录/执行登录
def login(request):
    if request.method == "GET":
        return render(request,"user_login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("username")

#      验证账号和密码
        res = UserModel.objects.filter(username=username)
        if res.exists(): #存在,继续验证密码
            user =  res.first()
            # user = UserModel()
            if user.passward == create_pass(password):#密码也匹配
                 # 设置一个session
                request.session["user_id"] = user.id

                # 重定向到首页
                return redirect(reverse("app:mineindex"))

        return redirect(reverse("app:login"))

