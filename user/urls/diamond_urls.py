from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.diamonds_views.diamond_product import *
from user.views.diamonds_views.diamonds_filters import *

urlpatterns = [
    # All objects of colorstones
    
    # Single Diamond
    path("showDiamond/<int:product_id>", showDiamond, name="showDiamond"),
    path("diamondFilter", diamondFilter.as_view(), name="diamondFilter"),
]
