from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

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
    path('deleteid<int:idno>',views.deleteid,name="deleteid"),
    path('showform1',views.showform1,name="showform1"),
    path('showform2',views.showform2,name="showform2"),
    path('updateJ/<str:pk>/', views.updateJ, name="updateJ"),
    path('deleteid_d<int:idno>',views.deleteid_d,name="deleteid_d"),
    path('update_d/<str:dk>/', views.update_d, name="update_d"),
    path('showcs',views.showcs,name="showcs"),
    path('update_cs/<str:ck>/', views.update_cs, name="update_cs"),
    path('deleteid_cs<int:idno>',views.deleteid_cs,name="deleteid_cs"),
    path('cform',views.cform,name="cform"),
    path('showinvj',views.showinvj,name="showinvj"),
    path('returninvj/<str:id1>',views.returninvj,name="returninvj"),
    path('addjtocart/<str:primkey>',views.addjtocart,name="addjtocart"),
    
    # path('search',views.search,name="search"),

    # path(r'^delete/(?P<idno>\d+)/$',views.deleteid, name='deleteid')
]
