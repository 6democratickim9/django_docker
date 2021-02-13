from django.urls import path
from .views import *

app_name = 'it_news'

urlpatterns = [
    path('', NewsLV.as_view(), name='post_all'),
    # path('refresh', RefreshFormView.as_view(), name='refresh'),
    path('search/', SearchFormView.as_view(), name='post_search'),
    path('refresh/', RefreshFormView.as_view(),name='refresh')
    
    
]