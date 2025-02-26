"""
URL configuration for Sales_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/',include('sales.urls')),


]

'''
在manage.py启动之后就可以使用以下的代码来进行特定路由的测试工作，不需要来添加端口来测试。ok?
http://localhost/sales/customers/

进度条：1月9日最后https://www.byhy.net/py/django/07/到达登录界面的工作中。
'''