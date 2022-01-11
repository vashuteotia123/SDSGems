
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.colorstone_views.colostone_product import *
from user.views.colorstone_views.colorstone_filters import *


urlpatterns = [
    # All objects of colorstones
  
    # Filters for ColorStones

    # ColorStone Details
    path('showColorStone/<int:product_id>',
         showColorStone, name="showColorStone"),

    # Colorstone filter
    path('colorStoneFilter', colorStoneFilter.as_view(), name="colorStoneFilter"),

]
