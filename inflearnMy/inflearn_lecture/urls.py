
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_list, name="home_list"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('lecture_list/', views.lecture_list, name="lecture_list"),
    path('lecture_list/<int:pk>/', views.lecture_detail, name="lecture_detail"),
]
