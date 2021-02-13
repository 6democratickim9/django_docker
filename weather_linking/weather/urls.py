from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('weather/', views.index, name='weather'),  #the path for our index view
    path('save/', views.save_weather),
    path('view/', views.view_weather),
    
]
