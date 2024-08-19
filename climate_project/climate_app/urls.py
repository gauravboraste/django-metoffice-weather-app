from django.urls import path
from .views import fetch
from . import views
from .views import get_data

urlpatterns = [
   
    path('',views.fetch, name='all_chai'),
    path('get_data/', views.get_data, name='get_data'),
    
    
]