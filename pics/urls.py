from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.pics_of_day, name = 'picsToday'),
    path('detail/<int:pkid>', views.pics_details, name = 'detail'),
    path('archives/<str:past_date>', views.past_days_pics, name = 'pastPics'),
    path('search/', views.search_results, name = 'search_results'),
    path('pics/<int:pics_id>',views.pics,name ='pics'),
]
