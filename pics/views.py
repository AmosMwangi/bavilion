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

# display past days pics
def past_days_pics(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(picsToday)

    bird = Pics.days_pics(date)
    return render(request, 'all-pics/past-pics.html', {"date":date,"bird":bird, "title":"Past News"})

