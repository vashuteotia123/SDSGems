
from django.urls import path
from user.views import common_views
from django.urls.resolvers import URLPattern
from user.views.common_views import *
from user.views.jewellery_views.jewellery_product import *
from user.views.jewellery_views.jewellery_filters import *

urlpatterns = [
    # All objects of Jewellery

    # Single Jewellery
    path('showJewellery/<int:product_id>', showJewellery, name='showJewellery'),

    # Jewellery Filter
    path('jewelleryFilter', jewelleryFilter.as_view(), name='jewelleryFilter'),
]
