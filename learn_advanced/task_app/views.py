from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


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
