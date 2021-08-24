from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from firstapp.views import *

urlpatterns = [
    path('',views.index,name="index"),
    path('second',views.index2,name="second"),
    path('takeinput',views.take_input,name="takeinput"),
    path('show_data',views.show_data,name="show_data"),
    path('showform',views.showform,name="showdform"),
    path('formsubmit',views.formsubmit,name="formsubmit"),
    # path('ajax/load-currency/',views.load_currency,name="ajax/load-currency/")
    path('showj',views.showjewell,name="showjewell"),
    path('showd',views.showdiamond,name="showdiamond"),
    path('returnid<int:idno>',views.returnid,name="returnid"),
    path('deleteid<int:idno>',views.deleteid,name="deleteid"),
    path('showform1',views.showform1,name="showform1"),
    path('showform2',views.showform2,name="showform2"),
    path('returnid_d<int:idno>',views.returnid_d,name="returnid_d"),
    path('updateJ/<str:pk>/', views.updateJ, name="updateJ"),
    path('deleteid_d<int:idno>',views.deleteid_d,name="deleteid_d"),
    path('update_d/<str:dk>/', views.update_d, name="update_d"),
    path('showcs',views.showcs,name="showcs"),
    path('update_cs/<str:ck>/', views.update_cs, name="update_cs"),
    path('returnid_cs<int:idno>',views.returnid_cs,name="returnid_cs"),
    path('deleteid_cs<int:idno>',views.deleteid_cs,name="deleteid_cs"),
    path('cform',views.cform,name="cform"),
    path('delete/search',views.search,name="search"),
    # path('delete/',Jewellery_view.as_view(),name="delete-jewell"),
    path('showinv_d',views.showinv_d,name="showinv_d"),
    path('showinv_cs',views.showinv_cs,name="showinv_cs"),
    # path('returninvj/<str:id>',views.returninvj,name="returninvj"),
    # path('returninv_d/<str:id1>',views.returninv_d,name="returninv_d"),
    # path('returninv_cs/<str:id1>',views.returninv_cs,name="returninv_cs"),
    path('showcart',views.showcart,name="showcart"),
    # path('sell_POJ', views.sell_POJ,name="sell_POJ"),
    path('addtocart<str:id>',Jewellery_view.addtocart,name="addtocart"),
    path('delete/',Jewellery_view.as_view(),name="delete-jewell"),
    path('returnj<str:id>',Jewellery_view.returnj,name="returnj"),
    path('retobj_j',views.retobj_j,name="retobj_j"),
    # path('displayinv',views.displayinv,name="displayinv"),
    # path('search',views.Jewellery_view.as_view(),name="search"),
    
    # path('search',views.search,name="search"),

    # path(r'^delete/(?P<idno>\d+)/$',views.deleteid, name='deleteid')
]
