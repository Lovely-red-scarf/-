"""four URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from first import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('add_book/',views.add_book,name='add_book'),

    re_path('del_book/',views.del_book ,name='del_book'),

    re_path('edit_book/(\d+)/',views.edit_book,name = 'edit_book'),


    path('login/',views.login_session,name='login'),

    path('logout/',views.logout,name = 'logout'),
    path('register/',views.register, name = 'register'),
    path('hint/',views.hint,name = 'hint'),#这个是你的 跳转注册的界面
    path('',views.login_session),  #等你输入为空的时候让你进去 login界面



]
