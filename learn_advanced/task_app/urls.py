"""
URL configuration for task_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from task_app import views

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.CategoryViewSet)
# /categorys/ --> list --> GET --> lay danh sach Category
# /categorys/ --> list --> POST --> them Category moi
# /categorys/{category_id} --> detail --> GET --> xem chi tiet 1 Category
# /categorys/{category_id} --> detail --> PUT --> cap nhat 1 Category
# /categorys/{category_id} --> detail --> DELETE --> xoa 1 Category

urlpatterns = [
    path("", views.index, name="index"),
    path('welcome/', views.welcome, name='welcome'),
    path('test/', views.TestView.as_view(), name='test'),


    path('api/', include(router.urls)),
]
