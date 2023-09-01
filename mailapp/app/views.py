from django.http import HttpResponse
from django.template import loader
from app.models import Messages


def app(request):
    messages = Messages.objects.all()
    template = loader.get_template('app.html')
    total_marked_messages = Messages.objects.filter(is_marked=True).count()
    context = {
        'messages': messages,
        'total_marked_messages': total_marked_messages,
    }
    return HttpResponse(template.render(context, request))
