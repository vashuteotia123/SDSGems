
from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from user.views import *

urlpatterns = [
    #user model 

    path('user_register', views.SignUpView.as_view(), name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_Logout, name="user_logout"),
    path('', views.home, name="home"),
    path('shop_list', ShopList.as_view(), name="shop_list"),
    path('blog_list', BlogList.as_view(), name="blog_list"),
    path('contact_us', ContactUs.as_view(), name="contact_us"),
    path('myaccount', MyAccount.as_view(), name="myaccount"),

    #Filters for ColorStones
    path('colorStoneByShapeFilter/<int:shape_id>', colorStoneByShapeFilter, name="colorStoneByShapeFilter")

]