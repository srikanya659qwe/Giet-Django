"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.sample,name='sample'),
    path('hello/',views.hlo,name='hello'),
    path('dynamic/<int:id>/',views.dynamic,name='dynamic'),
    path('task/<str:name>/',views.task,name='task'),
    path('home/<int:id>/<str:name>/',views.home,name='home'),



    path('temp/',views.temp,name='temp'),
    path('table/',views.table,name='table'),
    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external'),


    path('boot/',views.boot,name='boot'),
    path('register/',views.register,name='register'),
    path('offlinebt/',views.offline,name='offline'),



    path('reg/',views.reg,name='reg'),
    path('display/',views.display,name='display'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]
