"""NightSky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import main.views
from accounts import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('main/', main.views.main, name="main"),
    path('accounts/', user_views.register, name="register"),
    path('accounts/login/', user_views.login, name="login"),
    path('accoutns/logout/', user_views.logout, name="logout"),
    path('comment/<int:index>/delete/<int:cindex>/',main.views.comment_delete, name="comment_delete"),
    path('comment/<int:index>/edit/<int:cindex>/', main.views.comment_edit, name="comment_edit"),
    path('mysky/', main.views.mysky, name="mysky"), 
    path('realmain/', main.views.realmain, name="realmain"),
    path('mysky/user_update/', main.views.user_update, name="user_update"),
    path('mysky/user_update/changeid/', main.views.change_ID, name="change_ID"),
    path('mysky/user_update/changeemail/', main.views.change_Email, name="change_Email"),
    path('mysky/user_update/changepw/', main.views.change_pw, name="change_pw"),
    path('mysky/mysearch/', main.views.mysearch, name="mysearch"),

]
