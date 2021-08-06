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
    path('deleteid<int:idno>',views.deleteid,name="deleteid"),
    path('showform2',views.showform2,name="showform2"),
    path('updateJ/<str:pk>/', views.updateJ, name="updateJ"),
    # path(r'^delete/(?P<idno>\d+)/$',views.deleteid, name='deleteid')
]
