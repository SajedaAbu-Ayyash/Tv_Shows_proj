from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('add_show', views.new_show),
    path('submit_show', views.submit_show),
    path('display_show', views.display_show)
    	   
]
