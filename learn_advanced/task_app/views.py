from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer


def index(request):
    # return HttpResponse('Hello World!')
    return render(request,
                  template_name='index.html',
                  context={'name': 'HV'}, )


def welcome(request):
    return HttpResponse('Hello')


class TestView(View):
    def get(self, request):
        return HttpResponse('Test')

    def post(self, request):
        pass


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # list --> GET --> xem danh sach Category
    # list --> POST --> them 1 Category
    # detail --> GET --> PK --> xem chi tiet 1 Category
    # detail --> PUT --> PK --> cap nhat 1 Category
    # delete --> PK --> xoa 1 Category

    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
