
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.colorstone_views.colorstone_home_filters import *
from user.views.colorstone_views.colostone_product import *
from user.views.colorstone_views.colorstone_filters import *


urlpatterns = [
    # All objects of colorstones
    path('allColorStones', allColorStones, name='allColorStones'),
    path('allColorStones/<int:page>', allColorStones, name='allColorStones'),
    # Filters for ColorStones

    path('colorStoneByShapeFilter/<int:shape_id>',
         colorStoneByShapeFilter, name="colorStoneByShapeFilter"),
    path('colorStoneByShapeFilter/<int:shape_id>/<int:page>',
         colorStoneByShapeFilter, name="colorStoneByShapeFilter"),
    path('colorStoneGemTypeFilter/<int:gemtype_id>', colorStoneGemTypeFilter,
         name="colorStoneGemTypeFilter"),
    path('colorStoneGemTypeFilter/<int:gemtype_id>/<int:page>',
         colorStoneGemTypeFilter, name="colorStoneGemTypeFilter"),
    path('colorStoneByOriginFilter/<int:origin_id>', colorStoneByOriginFilter,
         name="colorStoneByOriginFilter"),
    path('colorStoneByOriginFilter/<int:origin_id>/<int:page>',
         colorStoneByOriginFilter, name="colorStoneByOriginFilter"),
    path('colorStoneByColourFilter/<int:colour_id>', colorStoneByColourFilter,
         name="colorStoneByColourFilter"),
    path('colorStoneByColourFilter/<int:colour_id>/<int:page>',
         colorStoneByColourFilter, name="colorStoneByColourFilter"),

    # ColorStone Details
    path('showColorStone/<int:product_id>',
         showColorStone, name="showColorStone"),

    # Colorstone filter
    path('colorStoneFilter', colorStoneFilter.as_view(), name="colorStoneFilter"),
    path('colorStoneFilter/<int:page>',
         colorStoneFilter.as_view(), name="colorStoneFilter"),
]
