
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.jewellery_views.jewellery_home_filters import *
from user.views.jewellery_views.jewellery_product import *

urlpatterns = [
    # All objects of Jewellery
    path('allJewellery', allJewellery, name='allJewellery'),
    path('allJewellery/<int:page>', allJewellery, name='allJewellery'),
    # Filters for Jewellery
    path('JewelleryByCenterStoneFilter/<int:center_stone_id>',
         JewelleryByCenterStoneFilter, name="JewelleryByCenterStoneFilter"),
    path('JewelleryByCenterStoneFilter/<int:center_stone_id>/<int:page>',
         JewelleryByCenterStoneFilter, name="JewelleryByCenterStoneFilter"),
    path('JewelleryByMetalFilter/<int:metal_id>',
         JewelleryByMetalFilter, name="JewelleryByMetalFilter"),
    path('JewelleryByMetalFilter/<int:metal_id>/<int:page>',
         JewelleryByMetalFilter, name="JewelleryByMetalFilter"),
    path('JewelleryByJewelleryTypeFilter/<int:jewellery_type_id>',
         JewelleryByJewelleryTypeFilter, name="JewelleryByJewelleryTypeFilter"),
    path('JewelleryByJewelleryTypeFilter/<int:jewellery_type_id>/<int:page>',
         JewelleryByJewelleryTypeFilter, name="JewelleryByJewelleryTypeFilter"),

    # Single Jewellery
    path('showJewellery/<int:product_id>', showJewellery, name='showJewellery'),
]
