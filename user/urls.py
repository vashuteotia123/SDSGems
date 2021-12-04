
from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from firstapp.views import *

urlpatterns = [
    #user model 

    path('user_register', views.SignUpView.as_view(), name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_Logout, name="user_logout")
]