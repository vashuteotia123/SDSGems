
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.diamonds_views.diamond_product import *
from user.views.diamonds_views.diamonds_home_filters import *
from user.views.diamonds_views.diamonds_filters import *

urlpatterns = [
    # All objects of colorstones
    path('allDiamonds', allDiamonds, name='allDiamonds'),
    path('allDiamonds/<int:page>', allDiamonds, name='allDiamonds'),
    # Filters for ColorStones

    path('diamondByShapeFilter/<int:shape_id>',
         diamondByShapeFilter, name="diamondByShapeFilter"),
    path('diamondByShapeFilter/<int:shape_id>/<int:page>',
         diamondByShapeFilter, name="diamondByShapeFilter"),
    path('diamondByColorOriginFilter/<int:color_origin_id>',
         diamondByColorOriginFilter, name="diamondByColorOriginFilter"),
    path('diamondByColorOriginFilter/<int:color_origin_id>/<int:page>',
         diamondByColorOriginFilter, name="diamondByColorOriginFilter"),
    path('diamondByCutFilter/<int:cut_id>',
         diamondByCutFilter, name="diamondByCutFilter"),
    path('diamondByCutFilter/<int:cut_id>/<int:page>',
         diamondByCutFilter, name="diamondByCutFilter"),

    # Single Diamond
    path('showDiamond/<int:product_id>', showDiamond, name='showDiamond'),
    path('diamondfilter', diamondfilter.as_view(), name="diamondfilter"),
    path('diamondfilter/<int:page>',
         diamondfilter.as_view(), name="diamondfilter"),
]
