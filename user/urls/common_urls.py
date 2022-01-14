
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *

urlpatterns = [
    # user model

    path('user_register', common_views.SignUpView.as_view(), name="user_register"),
    path('user_login', common_views.user_login, name="user_login"),
    path('user_logout', common_views.user_Logout, name="user_logout"),
    path('', common_views.home, name="home"),
    path('contact_us', ContactUs.as_view(), name="contact_us"),
    path('myaccount', MyAccount.as_view(), name="myaccount"),
    path('about_us', aboutus, name="about_us"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
    path('terms_and_conditions', terms_and_conditions,
         name="terms_and_conditions"),
    path('return_and_exchange', return_and_exchange, name="return_and_exchange"),

    # Instant Quote
    path('instant_quote', instant_quote, name="instant_quote"),

    # Subscribed_users
    path('subscribe_newsletter', subscribe_newsletter,
         name="subscribe_newsletter"),

    # Searching
    path('SearchForUser', SearchForUser, name="SearchForUser"),

    # Conversion Rate for currency conversion
    path('getConversionRate', getConversionRate, name="getConversionRate"),

    # Forgot password
    path('forgot_password', forgot_password, name="forgot_password"),
    path('reset_password/<str:email>/<str:hash>',
         reset_password, name="reset_password"),

    # birthstone_list
    path('birthstone_list', birthstone_list, name="birthstone_list"),
    # birthstone_single
    path('birthstone_single/<int:birthstone_id>',
         birthstone_single, name="birthstone_single"),
]
