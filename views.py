from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from cinemas.models import Cinema, Show, Comment
import datetime

def menu(request):
    if 'id' in request.GET:
        print(type(request.GET['id']))
        c = Cinema.objects.get(id=request.GET['id'])
        return render(request, 'menu.html', locals())
    else:
        return HttpResponseRedirect("/cinemas_list/")


def list_cinemas(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas_list.html', locals())


def comment(request, id):
    if id:
        c = Cinema.objects.get(id=id)
    else:
        return HttpResponseRedirect("/cinemas_list/")
    if 'ok' in request.POST:
        user = request.POST['user']
        content = request.POST['content']
        email = request.POST['email']
        date_time = datetime.datetime.now()
        Comment.objects.create(user=user, email=email, content=content, date_time=date_time, cinema=c)  
    return render(request, 'comments.html', locals())