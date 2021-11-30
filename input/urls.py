from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('maxcurrent/', views.maxcurrent, name="maxcurrent"),
    path('chargetime/', views.chargetime, name="chargetime"),
    path('batterychoose/', views.batterychoose, name="batterychoose"),
]

urlpatterns+=staticfiles_urlpatterns()