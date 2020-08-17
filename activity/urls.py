from django.urls import  path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showlist/', views.showlist, name='activitylist'),
    #path(r'^showlist/(?P<start_time>\w{0,2})/$', views.showlist, name='activitylist'),
    #path('showlist/<int:start_time>', views.showlist, name='activitylist'),
    # ex: /activity/5
    path('<int:item_id>/', views.detail, name='detail'),
    # ex: /activity/5/duration
    path('<int:item_id>/', views.timeinfo, name='duration'),
]
