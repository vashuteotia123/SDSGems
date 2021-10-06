from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from firstapp.views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('second', views.index2, name="second"),
    path('takeinput', views.take_input, name="takeinput"),
    path('show_data', views.show_data, name="show_data"),
    path('showform', views.showform, name="showdform"),
    path('formsubmit', views.formsubmit, name="formsubmit"),
    # path('ajax/load-currency/',views.load_currency,name="ajax/load-currency/")
    path('showj', views.showjewell, name="showjewell"),
    path('showd', views.showdiamond, name="showdiamond"),
    path('returnid<int:idno>', views.returnid, name="returnid"),
    path('deleteid<int:idno>', views.deleteid, name="deleteid"),
    path('backtoinv<int:id>', views.backtoinv, name="backtoinv"),
    path('showform1', views.showform1, name="showform1"),
    path('showform2', views.showform2, name="showform2"),    
    path('updateJ/<str:pk>/', views.updateJ, name="updateJ"),        
    path('cform', views.cform, name="cform"),    
    path('addtocart<str:id>', Jewellery_view.addtocart, name="addtocart"),
    path('delete/', Jewellery_view.as_view(), name="delete-jewell"),    
    path('retobj_j', views.retobj_j, name="retobj_j"),    
    path('search', views.search, name="search"),    
    path('show_jewel_cart', saving_jewel_cart, name='show_jewel_cart'),
    path('show_jewel_form',BirdAddView.as_view(), name="show_jewel_form"),
    path('sell_jewel', views.sell_jewel, name='sell_jewel'),
    path('return_jewel_Inventory<int:id>', views.return_jewel_Inventory, name="return_jewel_Inventory"),
    path('return_jewel_cart<str:id>',views.return_jewel_cart, name='return_jewel_cart'),
    # path('delete/search',views.search,name="search"),
    # path('delete/',Jewellery_view.as_view(),name="delete-jewell"),
    # path('returninvj/<str:id>',views.returninvj,name="returninvj"),
    # path('returninv_d/<str:id1>',views.returninv_d,name="returninv_d"),
    # path('returninv_cs/<str:id1>',views.returninv_cs,name="returninv_cs"),
    # path('showcart', views.showcart, name="showcart"),
    # path('sell_POJ', views.sell_POJ,name="sell_POJ"),
    #  path('delete/search',views.search,name="search"),
    # path('search',views.search,name="search"),
    # path(r'^delete/(?P<idno>\d+)/$',views.deleteid, name='deleteid')
    # path('returnj<str:id>',Jewellery_view.returnj,name="returnj"),
    # path('displayinv',views.displayinv,name="displayinv"),


    # ////////////colorstones url////////////

    path('showcs', views.showcs, name="showcs"),
    path('update_cs/<str:ck>/', views.update_cs, name="update_cs"),    
    path('returnid_cs<int:idno>', views.returnid_cs, name="returnid_cs"),
    path('deleteid_cs<int:idno>', views.deleteid_cs, name="deleteid_cs"),
    path('search_cs', views.search_cs, name="search_cs"),        
    path('retobj_cs', views.retobj_cs, name="retobj_cs"),
    path('sell_cs', views.sell_cs, name='sell_cs'),
    path('show_colorstone_form',CSAddView.as_view(), name="show_colorstone_form"),
    path('delete_cs/', colorstone_view.as_view(), name="delete-cs"),
    path('search_cs', views.search_cs, name="search_cs"),
    # path('showcart_cs', saving_colorstone_cart, name='showcart_cs'),
    path('show_colorstone_cart', saving_colorstone_cart, name='show_colorstone_cart'),
    path('addtocart_cs/<str:id>', colorstone_view.addtocart_cs, name="addtocart_cs"),
    path('backtoinvcs1/<str:id>',views.backtoinvcs1, name="backtoinvcs1"),
    path('return_colorstone_Inventory<int:id>', views.return_colorstone_Inventory, name="return_colorstone_Inventory"),
    path('return_colorstone_cart<str:id>',views.return_colorstone_cart, name='return_colorstone_cart'),

    # ///////diamond url/////////

    path('deleteid_d<int:idno>', views.deleteid_d, name="deleteid_d"),
    path('update_d/<str:dk>/', views.update_d, name="update_d"),
    path('returnid_d<int:idno>', views.returnid_d, name="returnid_d"),
    path('show_diamond_cart', saving_diamond_cart, name='show_diamond_cart'),    
    path('show_diamond_form',DiamondAddView.as_view(), name="show_diamond_form"),    
    path('sell_diamond', views.sell_diamond, name='sell_diamond'),
    path('return_diamond_Inventory<int:id>', views.return_diamond_Inventory, name="return_diamond_Inventory"),
    path('retobj_d', views.retobj_d, name="retobj_d"),
    path('sell_diamond', views.sell_diamond, name='sell_diamond'),
    path('show_diamond_form',DiamondAddView.as_view(), name="show_diamond_form"),
    path('delete_d/', Diamond_view.as_view(), name="delete-d"),
    path('search_d', views.search_d, name="search_d"),    
    path('show_diamond_cart', saving_diamond_cart, name='show_diamond_cart'),
    path('addtocart_d/<str:id>',Diamond_view.addtocart_d, name="addtocart_d"),
    path('backtoinv_d/<str:id>',views.backtoinv_d, name="backtoinv_d"),
    path('return_diamond_Inventory<int:id>', views.return_diamond_Inventory, name="return_diamond_Inventory"),
    # ////
    path('displaycart2', views.displaycart2, name='displaycart2'),
    path('returncart2', views.returncart2, name='returncart2'),
    path('displaysalesreturn', views.displaysalesreturn, name='displaysalesreturn'),

    path('displaycart2_cs', views.displaycart2_cs, name='displaycart2_cs'),
    path('returncart2_cs', views.returncart2_cs, name='returncart2_cs'),
    path('displaysalesreturn_cs', views.displaysalesreturn_cs, name='displaysalesreturn_cs'),

    path('displaycart2_d', views.displaycart2_d, name='displaycart2_d'),
    path('returncart2_d', views.returncart2_d, name='returncart2_d'),
    path('displaysalesreturn_d', views.displaysalesreturn_d, name='displaysalesreturn_d'),
    path('return_diamond_cart<str:id>',views.return_diamond_cart, name='return_diamond_cart'),

]
