
from django.urls import path, include
from . import views

app_name = 'search'


urlpatterns = [ 
  path('', views.PublicPostIndexView.as_view(), name='top'), 
  ]
