"""ExcellToPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('store/', store , name="store"),
    path('student/', student , name="student"),
    path('shop/', shop , name="shop"),
    path('col/', col, name="col"),
    path('checkout/', checkout, name="ch"),
    path('coll_c/', col_c, name="cl-c"),
    path('sh/', shop_c, name="sh-c"),
    path('sto/', store_c, name="sto-c"),
    path('stu/', stu_c, name="stu-c"),
    path('login/', log, name="log"),
    path('signin/', sign, name="sign"),
]
