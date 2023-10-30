from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser

from .models import Category, User
from .serializers import CategorySerializer, UserSerializer


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
        # if self.action in permissions:
        #     return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
