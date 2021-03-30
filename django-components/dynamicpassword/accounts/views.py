from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from utils.utils_tools import _do_get, _do_post

# add by shijin 20171122 增加log
import logging

logger = logging.getLogger('django.ops')


from ..env.settings import APPKEY, SSOServerDomain, SSOauthURL, SSOClientDomain, VERIFY_ACCOUNTS_URL, \
    GET_DEPARTMENT_URL, SSO_API_URL



# @log_inorout('login')
@csrf_exempt
def login_admin(request):
    _redirect_url = request.GET.get('next', '/')  # 获取重定向地址
    # print(request.build_absolute_uri())
    # print(request.get_full_path())
    _login_user = 'Guest'
    errors_list = []
    error_msg = ""
    if 'VALIDATE_SECRET' in SSO_API_URL.keys() and SSO_API_URL.get('VALIDATE_SECRET').get('enable'):
        username_placeholder = "请输入系统账号或邮箱账号"
        password_placeholder = "请输入密码加恒昌手机令牌"
    else:
        username_placeholder = "请输入邮箱账号"
        password_placeholder = "请输入密码"

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        # django 1.11之后authenticate方法增加了request参数
        user = authenticate(request, username=name, password=password)

        # 账号验证通过
        if user is not None and user.is_superuser:
            # 将user存入session
            auth_login(request, user)

            uu = request.user
            u = User.objects.get(username=uu)

            return HttpResponseRedirect(_redirect_url)

        # 账号验证未通过
        else:
            error_msg = '输入的用户名或密码错误'

    context = {'errors_list': errors_list, 'user_login': _login_user, 'error': error_msg,
               'username_placeholder': username_placeholder, 'password_placeholder': password_placeholder}
    return render(request, 'login.html', context)


@csrf_exempt
def logout(request):

    # log_instance = LogInfo(action='login').get_loginstance
    msg = dict(operate='logout', message='logout')

    access_token = request.session.get('access_token')

    if request.user.is_superuser and access_token is None:
        auth_logout(request)
        return HttpResponseRedirect(reverse('login'))

    url = SSOServerDomain + '/logout'  # 拼接url
    auth_logout(request)
    request.session.flush()
    data = dict(access_token=access_token)
    try:
        _do_post(url, **data)
    except:
        pass
    return HttpResponseRedirect(reverse('login'))


