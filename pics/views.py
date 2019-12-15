from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse,Http404
from .models import Pics

# display home 
def home(request):
 
    pics = Pics.todays_pics()
    return render(request, 'folder/home.html', {"pics":pics})

# display pic details 
def detail(request,pkid):
    try:
        image=Pics.objects.get(id=pkid)
    except DoesNotExist:
        raise Http404()

    return render(request, 'folder/details.html', {"image":image})

