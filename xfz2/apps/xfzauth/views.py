from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import LoginForm
from utils import restful
from django.views.decorators.csrf import csrf_exempt
from utils.captcha.xfzcaptcha import Captcha
from io import BytesIO


@csrf_exempt
# @require_POST
def login_view(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'common/login.html')

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=telephone, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if remember:
                        request.session.set_expiry(None)  # 选择记住我,使用django自带的session超时时间,2周
                    else:
                        request.session.set_expiry(0)  # 没选择记住我,浏览器关闭session失效

                    return render(request, 'news/index.html')

                else:
                    return restful.unauth(message="账号已经被冻结")
            else:
                return restful.params_error(message="手机号或密码错误")
        else:
            return restful.params_error(message=form.get_errors())


def logout_view(request):
    """
    退出登录
    :param request:
    :return:
    """
    logout(request)
    index_url = reverse('index')
    return redirect(index_url)


def img_captcha(request):
    """
    图片验证码
    :param request:
    :return:
    """

    text, image = Captcha.gene_code()
    out = BytesIO()  # BytesIO:相当于一个管道 储存图片的流对象
    image.save(out, 'png')  # 调用save方法 将image对象保存到BytesIO中
    out.seek(0)  # 将BytesIO的文件指针移动到最开始位置
    response = HttpResponse(content_type='image/png')
    response.write(out.read())  # 从BytesIO中读出图片数据, 保存到response write从头开始读,所以要out.seek()
    response['Content-length'] = out.tell()  # 获取文件指针的位置(文件的大小)
    return response


def register_view(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'common/register.html')
