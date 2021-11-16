from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='searchengine.index'),
    # path('search/', views.search, name="searchengine.search"),
    path('search/', views.search, name="searchengine.search"),
]
