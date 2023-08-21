from django.shortcuts import render


def say_hello(request):
    print('say_hello')
    return render(request, 'hello.html', {'name': 'Hảo'})
