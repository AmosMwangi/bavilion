from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('detail/<int:pkid>', views.detail, name = 'detail'),
    path('archives/<str:past_date>', views.past_days_pics, name = 'pastPics'),
    path('search/', views.search_results, name = 'search_results'),
    path('pics/<int:pics_id>',views.pics,name ='pics'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
