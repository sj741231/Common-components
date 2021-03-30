"""hccmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required

# 参考 django.contrib.admin.sites.py 中的 urls() 以及 urlpatterns的定义
from ..accounts.views import login_admin as admin_login, logout as admin_logout  # 修改admin的login 和 logout
admin_urls = admin.site.urls
admin_urls[0][1].callback = admin_login
admin_urls[0][2].callback = admin_logout

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin_urls),
    # url(r'^admin/', admin.site.urls),
]

