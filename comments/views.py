from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.utils import timezone
from .models import Comment
from .utils import get_client_ip


def index(request):
    """Show every comment with an available form"""
    all_comments = Comment.objects.order_by('-request_time')
    template = loader.get_template('comments/index.html')
    context = {
        'all_comments': all_comments,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    """Create new comment method"""
    if request.method == 'POST':
        message = request.POST['message']
        _ip = get_client_ip(request)
        timestamp = timezone.now()
        comment = Comment(request_time=timestamp,
                          request_ip=_ip,
                          message=message)
        comment.save()
    return redirect('/')
