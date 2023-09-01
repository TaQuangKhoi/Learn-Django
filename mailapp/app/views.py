from django.http import HttpResponse
from django.template import loader
from app.models import Messages


def app(request):
    messages = Messages.objects.all().values()
    template = loader.get_template('app.html')
    context = {
        'messages': messages,
    }
    return HttpResponse(template.render(context, request))
