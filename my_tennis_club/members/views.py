from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def members(request):
    return HttpResponse("Hello world!")
