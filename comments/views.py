from time import gmtime, strftime
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Comment
from .utils import get_client_ip


def index(request):
    """Show every comment with an available form"""
    if request.method == 'POST':
        message = request.POST['message']
        _ip = get_client_ip(request)
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        comment = Comment(request_time=timestamp,
                          request_ip=_ip,
                          message=message)
        comment.save()
    all_comments = Comment.objects.order_by('-request_time')
    template = loader.get_template('comments/index.html')
    context = {
        'all_comments': all_comments,
    }
    return HttpResponse(template.render(context, request))
