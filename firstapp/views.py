from django.views.generic import View
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.utils.regex_helper import Group
from django.views.generic.base import TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
import re
import csv,io
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'second.html')


def take_input(request):
    user_name = request.POST.get("user_name")
    email_id = request.POST.get("email_id")
    newinput = Database(username=user_name, email=email_id)
    newinput.save()
    return render(request, 'second.html')


def show_data(request):
    context = {
        "all_data": Database.objects.all(),
        "countone": Database.objects.all().count(),
    }
    return render(request, "show_data.html", context=context)


def showform(request):
    latest = POJ.objects.last()
    form = POJForm(request.POST, initial={'stockid': latest.id})
    # countone=POJ.objects.all().count()
    # print(countone)
    if(form.is_valid()):
        form.save()
        return render(request, "index.html")
    context = {
        "formshow": form,
        "latest": POJ.objects.last()
    }
    return render(request, "form.html", context=context)


def formsubmit(request):
    return render(request, "index.html")


def showform1(request):
    form1 = POCSForm(request.POST)
    if(form1.is_valid()):
        #   new_object = invrt(jeweltype=form.cleaned_data['jeweltpye'], pieces=form.cleaned_data['pieces'])
        #     obj1=Inventoryofcolorstones.objects.create(location=form.cleaned_data['location'],shape=form.cleaned_data['shape'],gem_type=form.cleaned_data['gem_type']
        #     ,weight=form.cleaned_data['weight'],origin=form.cleaned_data['origin'],treatment=form.cleaned_data['treatment']
        #     ,certificate_no_cs=form.cleaned_data['certificate_no_cs'],color=form.cleaned_data['color'],measurements=form.cleaned_data['measurements']
        #     ,lab=form.cleaned_data['lab'],tag_price_cs=form.cleaned_data['tag_price_cs'])

        form1.save()
        return render(request, "index.html")
    context = {
        "formshow1": form1,
    }
    return render(request, "form1.html", context=context)


def showform2(request):
    form2 = PODForm(request.POST)
    if(form2.is_valid()):

        form2.save()
        return render(request, "index.html")
    context = {
        "formshow2": form2,
    }
    return render(request, "form2.html", context=context)

# def load_currency(request):
#     country_id = request.POST.get("country_id")
#     currency = currencies.objects.filter(country_id=country_id).all()
#     return render(request, 'templates/currency_dropdown_list_options.html', {'currency' : currency})

#  Jewellary Function 

def deleteid(request, idno):
    current = POJ.objects.get(id=idno)
    jstr = "J-"+str(idno)
    print(jstr)
    current_invj =Inventoryofjewellery.objects.get(stockid=jstr)
    current.delete()
    current_invj.delete()
    return render(request, "delete.html")

def returnid(request, idno):
    print("called")
    current = POJ.objects.all()
    context = {
        "returnjewel": current,
    }
    return render(request, "returnj.html", context=context)


def updateJ(request, pk):

    jewel_obj = POJ.objects.get(id=pk)
    form3 = POJForm(instance=jewel_obj)
    # print("7")
    if request.method == 'POST':
        # print("2")
        form3 = POJForm(request.POST, instance=jewel_obj)
        # print("3")
        form3.save()
        return redirect('/showj')

    context = {'form3': form3}
    return render(request, 'update_jewellery.html', context)


def showjewell(request):
    objjewell = POJ.objects.all()
    context = {
        "showjewellery": objjewell,
    }
    return render(request, "showj.html", context=context)

# def delete(request, idno):
#     query = Inventoryofjewellery.objects.get(pk=idno)
#     query.delete()
#     return HttpResponse("Deleted!")







def cform(request):
    comform = CompanyForm(request.POST)
    if(comform.is_valid()):

        comform.save()
        return render(request, "index.html")
    context = {
        "comform": comform,
    }
    return render(request, "cform.html", context=context)

###




# def returninvj(request, id):
#     now = Inventoryofjewellery.objects.get(id=id)
#     if now.appvreturnstatus is False:
#         now.appvreturnstatus==True
#     return redirect("/")

def retobj_j(request):
    objectsj = Inventoryofjewellery.objects.filter(appvreturnstatus=True)
    context = {
        "returned": objectsj,
    }
    return render(request, "returnj.html", context=context)





def returninv_cs(request, id1):
    now = Inventoryofcolorstones.objects.get(id=id1)
    # item = returnid(request, id1)
    context = {
        'returncs': now,
    }
    now.delete()

    return render(request, 'return_cs.html', context=context)

# def search(request):
#     posts = Inventoryofjewellery.objects.all()
#     search_term = ''
#     print("ABCD")
#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         posts = posts.filter(Q(id__icontains=search_term) | Q(jewellery_type__icontains=search_term))
#         context={
#             "showvalue":posts,

#         }
#         return render(request,"search.html",context=context)
#     else:
#         return render(request,".html",{})


# def addjtocart(request, primkey):

#     j_obj = Inventoryofjewellery.objects.get(id=primkey)
#     new_object = cloneInvofjewellery.objects.create(stockid=j_obj.stockid, location=j_obj.location, jewellery_type=j_obj.jewellery_type, center_stone=j_obj.center_stone,
#                                                     shape=j_obj.shape, metal=j_obj.metal, gross_wt=j_obj.grosswt, certificate=j_obj.cert,
#                                                     PCS=j_obj.pcs, tag_price=j_obj.tag_price)
#     return redirect('/showinvj')


# def showcart(request):
#     total = cloneInvofjewellery.objects.all()
#     global formlist
#     form_list = []
#     for i in total:
#         form_list.append(ADCForm(instance=i))
#     if request.method == "POST":

#         for item in form_list:
#             print(item)
#         return render(request, "showcart.html")
#     context = {
#         "totalitems": form_list,
#     }
#     return render(request, "showcart.html", context=context)


def search(request):
    print("hello")
    posts = Inventoryofjewellery.objects.all()
    search_term = ''
    search_term = request.POST.get('search')
    posts = posts.filter(Q(location__icontains=search_term) | Q(id__icontains=search_term)
                         )
    context = {
        "productsj": posts,

    }
    return render(request, "showinvj.html", context=context)
    # else:
    #     context = {
    #         "productsj": Inventoryofjewellery.objects.all(),
    #     }
    #     return render(request, "showinvj.html", context)


class Jewellery_view(View):
    def get(self, request):
        allproduct = Inventoryofjewellery.objects.all().order_by('stockid')
        # allclonej = cloneInvofjewellery.objects.all()
        context = {
            "productsj": allproduct,

        }
        return render(request, "showinvj.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            jewell_ids = request.POST.getlist('id[]')
            for id in jewell_ids:
                j = Inventoryofjewellery.objects.get(id=id)
                j.appvreturnstatus = True
                j.save()
        return redirect('delete-jewell')

    def addtocart(self, id):
        print("hello")
        j_obj = Inventoryofjewellery.objects.get(id=id)
        z=j_obj.stockid
        x=re.findall("[0-9]+",z)
        idj = int(x[0])
        j_obj2 = POJ.objects.filter(id=idj)
        if j_obj.purchaseapv is False:
             j_obj2.update(purchase_approval=True)
        j_obj.cartstatus = True
        j_obj.save()
        print(j_obj.cartstatus)
        new_object = cloneInvofjewellery.objects.create(stockid=j_obj.stockid, location=j_obj.location, jewellery_type=j_obj.jewellery_type, center_stone=j_obj.center_stone,
                                                        shape=j_obj.shape, metal=j_obj.metal, gross_wt=j_obj.grosswt, certificate=j_obj.cert,
                                                        PCS=j_obj.pcs, tag_price=j_obj.tag_price)
        return redirect('/delete')

    

def backtoinv(request, id):
    myobj = Inventoryofjewellery.objects.get(id=id)
    myobj.appvreturnstatus = False
    myobj.save()
    totalobjs = Inventoryofjewellery.objects.filter(appvreturnstatus=True)
    return redirect('/retobj_j')

# def get_Datas(request):
#         if request.is_ajax():
#             q = request.GET.get('company_name', '')
#             Datas = companyinfo.objects.filter(company_name = q )[:20]
#             results = []
#             for Data in Datas:
#                 Data_json = {}
#                 Data_json['value'] = Data.company_name
#                 results.append(Data_json)
#             data = JsonResponse.dumps(results)
#         else:
#             data = 'fail'
#         mimetype = 'application/json'
#         return HttpResponse(data, mimetype)

        
def saving_jewel_cart(request):
    total = cloneInvofjewellery.objects.all()
    total_jewels = list(total.values())
    jewel_formset = ADCFormSet(initial = total_jewels)
    if request.method == "POST":
        curr_formset = ADCFormSet(data = request.POST)
        print(len(curr_formset))
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems": jewel_formset,
    }
    return render(request, "showcart.html", context=context)

def sell_jewel(request):
    jewellery_objects = cloneInvofjewellery.objects.all()
    for object in jewellery_objects:
        Salesofjewellery.objects.create(
            stockid=object.stockid, 
            company_name=object.company_name, 
            location=object.location, 
            jewellery_type=object.jewellery_type,
            center_stone=object.center_stone,
            shape=object.shape,
            metal=object.metal, 
            gross_wt=object.gross_wt, 
            certificate=object.certificate, 
            PCS=object.PCS, 
            amount=object.amount, 
            DIS=object.DIS, 
            DIS_amount=object.DIS_amount, 
            total_value=object.total_value, 
            currency=object.currency, 
            tag_price=object.tag_price,
            rate=object.rate,
            salesapprovalstatus=object.salesapprovalstatus)
        Inventoryofjewellery.objects.filter(stockid=object.stockid).delete()
    cloneInvofjewellery.objects.all().delete()
    context = {
        "sold_items" : Salesofjewellery.objects.all(),
    }
    return render(request, "show_sell_jewel_table.html", context = context)


def return_jewel_Inventory(request, id):
    object = Salesofjewellery.objects.get(pk = id)
    Inventoryofjewellery.objects.create(stockid=object.stockid, 

            location=object.location, 
            jewellery_type=object.jewellery_type,
            center_stone=object.center_stone,
            shape=object.shape,
            metal=object.metal, 
            grosswt=object.gross_wt, 
            cert=object.certificate, 
            pcs=object.PCS, 
            purchaseapv=True,
            cartstatus=False,
            appvreturnstatus=False,
            tag_price=object.tag_price,

      )
    Salesreturn.objects.create(
        company_name=object.company_name,
        stockid=object.stockid,
        location=object.location,
        jewellery_type=object.jewellery_type,

    )
    Salesofjewellery.objects.filter(pk=id).delete()
    context = {
        "productsj": Inventoryofjewellery.objects.all(),

    }
    return render(request, "showinvj.html", context=context)

def save_jewel_forms(request):

    poj_formset = POJFormSet(queryset=POJ.objects.none())
    if request.method == "POST":
        curr_formset = POJFormSet(data = request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems" : poj_formset,
    }
    return render(request, "show_jewel_form.html", context=context)
    
class BirdAddView(TemplateView):
    template_name = "show_jewel_form.html"

    def get(self, *args, **kwargs):
        formset = POJFormSet(queryset=POJ.objects.none())
        return self.render_to_response({'totalitems': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = POJFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect("/")

        return self.render_to_response({'totalitems': formset})   
def returncart2(request,id):
    myobject=cloneInvofjewellery.objects.get(id=id)
    invobj=Inventoryofjewellery.objects.get(stockid=myobject.stockid)
    invobj.cartstatus=False
    invobj.save()
    tjcart=cloneInvofjewellery.objects.all()
    if tjcart is None:
        context={
            "Cart is Empty":tjcart,
        }
        return render(request,"displaycart.html",context=context)

    else:
        context={
        "tjcart":tjcart,
        }
        return render(request,"displaycart.html",context=context)
def displaysalesreturn(request):
    ret_sj = Salesreturn.objects.all()
    context={
        "ret_sj":ret_sj,
    }
    return render(request,"salereturnjewellery.html",context=context)

def displaycart2(request):
    tjcart=cloneInvofjewellery.objects.all()
    if tjcart is None:
        context={
            "Cart is Empty":tjcart,
        }
        return render(request,"displaycart.html",context=context)

    else:
        context={
        "tjcart":tjcart,
        }
        return render(request,"displaycart.html",context=context)

def return_jewel_cart(request,id):
    rjc = cloneInvofjewellery.objects.get(id=id)
    rjc2 = Inventoryofjewellery.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv is False:
        x=re.findall("[0-9]+",rjc2.stockid)
        rdj = int(x[0])
        xy=POJ.objects.filter(id=rdj)
        xy.update(purchase_approval=False)
    rjc2.cartstatus=False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2')


# Color stones function

def showcs(request):
    cs_obj = PurchaseOfColorStones.objects.all()
    context = {
        "show_cs": cs_obj,
    }
    return render(request, "showcs.html", context=context)


def returnid_cs(request, idno):
    print("called")
    current = PurchaseOfColorStones.objects.all()
    context = {
        "returncs": current,
    }
    return render(request, "return_cs.html", context=context)


def update_cs(request, ck):

    cs_obj = PurchaseOfColorStones.objects.get(id=ck)
    form5 = POCSForm(instance=cs_obj)
    # print("7")
    if request.method == 'POST':
        # print("2")
        form5 = POCSForm(request.POST, instance=cs_obj)
        # print("3")
        form5.save()
        return redirect('/showcs')

    context = {'form5': form5}
    return render(request, 'update_cs.html', context)


# def deleteid_cs(request, idno):
#     current = PurchaseOfColorStones.objects.get(id=idno)
#     current.delete()
#     return render(request, "delete.html")

def deleteid_cs(request, idno):
    current = PurchaseOfColorStones.objects.get(id=idno)
    c_str = "C-"+str(idno)
    print(c_str)
    current_invcs =Inventoryofcolorstones.objects.get(stockid=c_str)
    current.delete()
    current_invcs.delete()
    return render(request, "delete_cs.html")


def showinv_cs(request):
    inv_csobj = Inventoryofcolorstones.objects.all()
    context = {
        "showinv_cs": inv_csobj,
    }
    return render(request, "showinvcs.html", context=context)


def retobj_cs(request):
    object_cs = Inventoryofcolorstones.objects.filter(appvreturnstatus_cs=True)
    context={
          "returned_cs": object_cs,
      }
    return render(request, "return_cs.html", context =context)

def backtoinvcs1(request, id):
     myobj = Inventoryofcolorstones.objects.get(id=id)
     myobj.appvreturnstatus_cs = False
     myobj.save()
     totalobjs = Inventoryofcolorstones.objects.filter(appvreturnstatus_cs=True)
     return redirect('/retobj_cs')

def saving_colorstone_cart(request):
    print("saving")
    total = cloneInvofcolorstones.objects.all()
    total_colorstones = list(total.values())
    colorstone_formset = ADCFormSet_cs(initial = total_colorstones)
    if request.method == "POST":
        curr_formset = ADCFormSet_cs(data = request.POST)
        print(len(curr_formset))
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems_cs": colorstone_formset,
    }
    return render(request, "showcart_cs.html", context=context)
def sell_cs(request):
    cs_objects = cloneInvofcolorstones.objects.all()
    for object in cs_objects:
        Salesofcolorstones.objects.create(
            stockid=object.stockid, 
            company_name=object.company_name, 
            location=object.location, 
            shape=object.shape,
            gem_type=object.gem_type,
            certificate_no=object.certificate_no,
            origin=object.origin,
            treatment=object.treatment,
            Clarity=object.Clarity, 
            color=object.color, 
            measurements=object.measurements,
            lab=object.lab, 
            PCS=object.PCS, 
            Weight_cs=object.Weight_cs,
            # price=object.price,
            # units_cs=object.units_cs,
            amount_cs=object.amount_cs, 
            DIS_cs=object.DIS_cs, 
            DIS_amount_cs=object.DIS_amount_cs, 
            total_value_cs=object.total_value_cs, 
            currency_cs=object.currency_cs, 
            tag_price_cs=object.tag_price_cs,
            rate_cs=object.rate_cs,
            salesapprovalstatus_cs=object.salesapprovalstatus_cs)
        Inventoryofcolorstones.objects.filter(stockid=object.stockid).delete()
    cloneInvofcolorstones.objects.all().delete()
    context = {
        "sold_items" : Salesofcolorstones.objects.all(),
    }
    return render(request, "show_sell_cs_table.html", context = context)



def return_colorstone_Inventory(request, id):
    print("called sales cs")
    object = Salesofcolorstones.objects.get(id = id)
    print(object.certificate_no)
    Inventoryofcolorstones.objects.create(
            stockid=object.stockid, 
            shape=object.shape,
            location=object.location, 
            gem_type=object.gem_type,            
            origin=object.origin,            
            treatment=object.treatment, 
            certificate_no =object.certificate_no , 
            PCS=object.PCS, 
            Clarity=object.Clarity,
            lab=object.lab,
            color=object.color,
            purchaseapv=True,
            Weight = object.Weight_cs,
            cartstatus=False,
            appvreturnstatus=False,
            tag_price=object.tag_price_cs,
            measurements=object.measurements,
      )

    Salesreturn_cs.objects.create(
        company_name=object.company_name,
        stockid=object.stockid,
        location=object.location,
        gem_type=object.gem_type,

    )
    Salesofcolorstones.objects.filter(pk=id).delete()
    context = {
        "products_cs": Inventoryofcolorstones.objects.all(),

    }
    return render(request, "showinvcs.html", context=context)

def save_colorstone_forms(request):
    pocs_formset = POCSFormSet(queryset=PurchaseOfColorStones.objects.none())
    if request.method == "POST":
        curr_formset = POCSFormSet(data = request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems_cs" : pocs_formset,
    }
    return render(request, "show_colorstone_form.html", context=context)
    
class CSAddView(TemplateView):
    template_name = "show_colorstone_form.html"

    def get(self, *args, **kwargs):
        formset = POCSFormSet(queryset=PurchaseOfColorStones.objects.none())
        return self.render_to_response({'totalitems_cs': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = POCSFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect("/")

        return self.render_to_response({'totalitems_cs': formset})

class colorstone_view(View):
    def get(self, request):
        print("hello")
        allproduct = Inventoryofcolorstones.objects.all().order_by('stockid')
        # allclone_cs = cloneInvofcolorstones.objects.all()
        context = {
            "products_cs": allproduct.order_by('stockid'),

        }
        return render(request, "showinvcs.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            cs_ids = request.POST.getlist('id[]')
            for id in cs_ids:
                j = Inventoryofcolorstones.objects.get(id=id)
                j.appvreturnstatus_cs = True
                j.save()
        return redirect('delete-cs')

    def addtocart_cs(self, id):
        print("hello")
        j_obj = Inventoryofcolorstones.objects.get(id=id)
        z=j_obj.stockid
        x=re.findall("[0-9]+",z)
        idcs = int(x[0])
        j_obj2 = PurchaseOfColorStones.objects.filter(id=idcs)
        if j_obj.purchaseapv is False:
            j_obj2.update(purchaseapv=True)
        j_obj.cartstatus = True
        j_obj.save()
        print(j_obj.cartstatus)       
        new_object = cloneInvofcolorstones.objects.create(stockid=j_obj.stockid, location=j_obj.location,shape=j_obj.shape, gem_type=j_obj.gem_type,
                                                            origin=j_obj.origin,treatment=j_obj.treatment, certificate_no=j_obj. certificate_no,
                                                            color=j_obj.color,measurements=j_obj.measurements,lab=j_obj.lab,PCS=j_obj.PCS,
                                                            Weight_cs=j_obj.Weight,tag_price_cs=j_obj.tag_price,Clarity=j_obj.Clarity)
        return redirect('/delete_cs')

#  extra function cs

def returncart2_cs(request,id):
    myobject=cloneInvofcolorstones.objects.get(id=id)
    invobj=Inventoryofcolorstones.objects.get(stockid=myobject.stockid)
    invobj.cartstatus=False
    invobj.save()
    tcscart=cloneInvofcolorstones.objects.all()
    context={
        "tcscart":tcscart,

    }
    return render(request,"displaycart_cs.html",context=context)

def displaysalesreturn_cs(request):
    ret_scs = Salesreturn_cs.objects.all()
    context={
        "ret_scs":ret_scs,
    }
    return render(request,"salereturncolorstones.html",context=context)

def displaycart2_cs(request):
    tcscart=cloneInvofcolorstones.objects.all()
    context={
        "tcscart":tcscart,
    }
    return render(request,"displaycart_cs.html",context=context) 

def return_colorstone_cart(request,id):
    rjc = cloneInvofcolorstones.objects.get(id=id)
    rjc2 = Inventoryofcolorstones.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv is False:
        x=re.findall("[0-9]+",rjc2.stockid)
        rdj = int(x[0])
        xy=PurchaseOfColorStones.objects.filter(id=rdj)
        xy.update(purchaseapv=False)
    rjc2.cartstatus=False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2_cs')

# Diamond Function 
def showdiamond(request):
    diamondobj = POD.objects.all()
    context = {
        "showdia": diamondobj,
    }
    return render(request, "showd.html", context=context)


def update_d(request, dk):

    diamond_obj = POD.objects.get(id=dk)
    form4 = PODForm(instance=diamond_obj)
    # print("7")
    if request.method == 'POST':
        # print("2")
        form4 = PODForm(request.POST, instance=diamond_obj)
        # print("3")
        form4.save()
        return redirect('/showd')

    context = {'form4': form4}
    return render(request, 'update_diamond.html', context)


def returnid_d(request, idno):
    print("called")
    current = POD.objects.all()
    context = {
        "returndiamond": current,
    }
    return render(request, "return_d.html", context=context)




def deleteid_d(request, idno):
    current = POD.objects.get(id=idno)
    d_str = "D-"+str(idno)
    print(d_str)
    current_invd =Inventoryofdiamond.objects.get(stockid=d_str)
    current.delete()
    current_invd.delete()
    return render(request, "delete_d.html")




def showinv_d(request):
    if request.session:
        inv_dobj = Inventoryofdiamond.objects.all()
        context = {
            "showinv_d": inv_dobj,
        }
        return render(request, "showinvd.html", context=context)
    

def returninv_d(request, id1):
    now = Inventoryofdiamond.objects.get(id=id1)
    # item = returnid(request, id1)
    context = {
        'returndiamond': now,
    }
    now.delete()

    return render(request, 'return_d.html', context=context)

def saving_diamond_cart(request):
    total = cloneInvofdiamond.objects.all()
    total_diamond = list(total.values())
    diamond_formset = ADCFormSet_d(initial = total_diamond)
    if request.method == "POST":
        curr_formset = ADCFormSet_d(data = request.POST)
        print(len(curr_formset))
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems_d": diamond_formset,
    }
    return render(request, "showcart_d.html", context=context)

def save_diamond_forms(request):

    pod_formset = PODFormSet(queryset=POD.objects.none())
    if request.method == "POST":
        curr_formset = PODFormSet(data = request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems_d" : pod_formset,
    }
    return render(request, "show_diamond_form.html", context=context)
    
class DiamondAddView(TemplateView):
    template_name = "show_diamond_form.html"

    def get(self, *args, **kwargs):
        formset = PODFormSet(queryset=POD.objects.none())
        return self.render_to_response({'totalitems_d': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = PODFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect("/")

        return self.render_to_response({'totalitems_d': formset})

def retobj_d(request):
    objects_d= Inventoryofdiamond.objects.filter(appvreturnstatus_d=True)
    context = {
        "returned_d": objects_d,
    }
    return render(request, "return_d.html",context=context)


class Diamond_view(View):
    def get(self,request):
        print("hello")
        allproduct = Inventoryofdiamond.objects.all().order_by('stockid')
        # allclone_d = cloneInvofdiamond.objects.all()
        context = {
            "products_d": allproduct,

        }
        return render(request, "showinvd.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            d_ids = request.POST.getlist('id[]')
            for id in d_ids:
                j = Inventoryofdiamond.objects.get(id=id)
                j.appvreturnstatus_d = True
                j.save()
        return redirect('delete-d')

    def addtocart_d(self, id):
        print("hello")
        j_obj = Inventoryofdiamond.objects.get(id=id)
        z=j_obj.stockid
        x=re.findall("[0-9]+",z)
        id_d = int(x[0])
        j_obj2 = POD.objects.filter(id=id_d)
        if j_obj.purchaseapv_d is False:
            j_obj2.update(purchaseapv_d=True)
        j_obj.cartstatus = True
        j_obj.save()
        print(j_obj.cartstatus)
        new_object = cloneInvofdiamond.objects.create(stockid=j_obj.stockid, location=j_obj.location,shape=j_obj.shape, clarity=j_obj.clarity,
                                                        white_color_grade1=j_obj.white_color_grade1,fancy_color_intensity1=j_obj.fancy_color_intensity1,fancycolor_grade=j_obj.fancycolor_grade, 
                                                        cut=j_obj.cut,polish=j_obj.polish,symmetry=j_obj.symmetry,measurements=j_obj.measurements,depth=j_obj.depth,table=j_obj.table,
                                                        fluorescence_intensity=j_obj.fluorescence_intensity,fluorescence_color=j_obj.fluorescence_color,certificate_no_d=j_obj. certificate_no_d,
                                                        certificate_d=j_obj.certificate_d,laser_inscription=j_obj.laser_inscription,PCS_d=j_obj.PCS_d,weight_d=j_obj.weight_d,units=j_obj.units,tag_price_d=j_obj.tag_price_d)
        return redirect('/delete_d')

def backtoinv_d(request,id):
    myobj = Inventoryofdiamond.objects.get(id=id)
    myobj.appvreturnstatus_d = False
    myobj.save()
    totalobjs = Inventoryofdiamond.objects.filter(appvreturnstatus_d=True)
    return redirect('/retobj_d')

def sell_diamond(request):
    diamond_objects = cloneInvofdiamond.objects.all()
    for object in diamond_objects:
        Salesofdiamond.objects.create(
            stockid=object.stockid, 
            company_name=object.company_name, 
            location=object.location, 
            shape=object.shape,
            clarity=object.clarity,
            color_origin1=object.color_origin1,
            white_color_grade1=object.white_color_grade1, 
            fancy_color_intensity1=object.fancy_color_intensity1, 
            # fancy_color_1=object.fancy_color_1,
            # fancy_color_2=object.fancy_color_2,
            fancycolor_grade=object.fancycolor_grade,
            cut=object.cut,
            polish=object.polish,
            symmetry=object.symmetry,
            measurements=object.measurements,
            depth=object.depth,
            table=object.table,
            fluorescence_intensity=object.fluorescence_intensity,
            fluorescence_color=object.fluorescence_color,
            certificate_no_d=object.certificate_no_d,
            certificate_d=object.certificate_d, 
            laser_inscription=object.laser_inscription,
            PCS_d=object.PCS_d, 
            weight_d=object.weight_d,
            units=object.units,
            amount_d=object.amount_d, 
            DIS_d=object.DIS_d, 
            DIS_Amount_d=object.DIS_Amount_d, 
            total_value_d=object.total_value_d, 
            currency=object.currency, 
            tag_price_d=object.tag_price_d,
            rate_d=object.rate_d,
            salesapprovalstatus_d=object.salesapprovalstatus_d)
            
        Inventoryofdiamond.objects.filter(stockid=object.stockid).delete()
    cloneInvofdiamond.objects.all().delete()
    context = {
        "sold_items" : Salesofdiamond.objects.all(),
    }
    return render(request, "show_sell_diamond_table.html", context = context)


def return_diamond_Inventory(request, id):
    object = Salesofdiamond.objects.get(pk = id)
    Inventoryofdiamond.objects.create(stockid=object.stockid, 
            fancy_color_intensity1=object.fancy_color_intensity1,
            location=object.location, 
            shape=object.shape,            
            clarity=object.clarity,
            white_color_grade1=object.white_color_grade1, 
            fancycolor_grade=object.fancycolor_grade, 
            certificate_no_d=object.certificate_no_d, 
            PCS_d=object.PCS_d, 
            purchaseapv_d=True,
            cartstatus=False,
            appvreturnstatus_d=False,
            tag_price_d=object.tag_price_d,
            cut=object.cut,
            polish=object.polish,
            symmetry=object.symmetry,
            measurements=object.measurements,
            depth=object.depth,
            table=object.table,
            fluorescence_intensity=object.fluorescence_intensity,
            fluorescence_color=object.fluorescence_color,
            certificate_d=object.certificate_d,
            laser_inscription=object.laser_inscription,
            weight_d=object.weight_d,
            units=object.units,
            price=object.price,


      )
    Salesreturn_d.objects.create(
        company_name=object.company_name,
        stockid=object.stockid,
        location=object.location,
        shape=object.shape,

    )
    Salesofdiamond.objects.filter(pk=id).delete()
    context = {
        "products_d": Inventoryofdiamond.objects.all(),

    }
    return render(request, "showinvd.html", context=context)

def return_diamond_cart(request,id):
    rjc = cloneInvofdiamond.objects.get(id=id)
    rjc2 = Inventoryofdiamond.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv_d is False:
        x=re.findall("[0-9]+",rjc2.stockid)
        rdj = int(x[0])
        xy=POD.objects.filter(id=rdj)
        xy.update(purchaseapv_d=False)
    rjc2.cartstatus=False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2_d')



# extra function d

def returncart2_d(request,id):
    myobject=cloneInvofdiamond.objects.get(id=id)
    invobj=Inventoryofdiamond.objects.get(stockid=myobject.stockid)
    invobj.cartstatus=False
    invobj.save()
    tdcart=cloneInvofdiamond.objects.all()
    context={
        "tdcart":tdcart,
    }
    return render(request,"displaycart_d.html",context=context)

def displaysalesreturn_d(request):
    ret_sd = Salesreturn_d.objects.all()
    context={
        "ret_sd":ret_sd,
    }
    return render(request,"salereturndiamond.html",context=context)

def displaycart2_d(request):
    tdcart=cloneInvofdiamond.objects.all()
    context={
        "tdcart":tdcart,
    }
    return render(request,"displaycart_d.html",context=context)

def jewellery_upload(request):
    template="jewelleryupload.html"
    if request.method=="GET":
        return render(request,template)

    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,"This is not a CSV file")
    dataset=csv_file.read().decode('UTF-8')
    io_string=io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string,delimiter=','):
        z=re.findall("[0-9]+",column[13])
        # datere=re.findall(r'\d{2}/\d{2}/\d{4}',column[0])
        # date_value=list(datere[0])
        # final_date=datetime.date(int(''.join(date_value[6:])),int(''.join(date_value[3:4])),int(''.join(date_value[0:2])))
        temp_date = datetime.strptime(str(column[0]), "%m-%d-%y").date()
        print(temp_date)
        # print(final_date)
        f=POJ
        try:
            f.company_name = companyinfo.objects.get(company_name=column[2])
        except ObjectDoesNotExist:
            html="Company Name does not exist " + '<a href="/showform">Create Company details</a>'
            return HttpResponse(html)
        print(f.company_name)
        try:
            f.location,lcobj = loc.objects.get_or_create(place=column[3].lower())
            if lcobj :
                f.location.save()
        except Exception as e:
            raise e
        print(f.location)
        try:
            f.jewellery,jlobj = jewell.objects.get_or_create(jewel=column[4].lower())
            if jlobj :
                f.jewellery.save()
        except Exception as e:
            raise e
        print(f.jewellery)
        try:
            f.center_stone,clobj = centerstone.objects.get_or_create(stone=column[5].lower())
            if clobj :
                f.center_stone.save()
        except Exception as e:
            raise e
        print(f.center_stone)
        try:
            f.color_of_center_stone,clsobj=colorofcstone.objects.get_or_create(color=column[6].lower()) 
            if clsobj :
                f.color_of_center_stone.save()
        except Exception as e:
            raise e
        f.color_of_center_stone=colorofcstone.objects.get(color=column[6]) 
        print(f.color_of_center_stone)
        try:
            f.shape,sobj=shape1.objects.get_or_create(shape=column[7].lower())     
            if sobj :
                f.shape.save()
        except Exception as e:
            raise e
      
        print(f.shape)
        try:
            f.metal,mobj = metal1.objects.get_or_create(metal=column[8].lower())
            if mobj :
                f.metal.save()
        except Exception as e:
            raise e
        
        print(f.metal)
        try:
            f.cert,cerobj = certificate.objects.get_or_create(cert=column[11].lower())
            if cerobj :
                f.cert.save()
        except Exception as e:
            raise e
    
        print(f.cert)
        try:
            f.currencyid,crobj = currencies.objects.get_or_create(currency=column[17].lower())
            if crobj :
                f.currencyid.save()
        except Exception as e:
            raise e
        print(column[17])
        print(column[19])
        print(f.currencyid)
        if(column[20]=="NO"):
    
            y=False
            print(y)
        else:
            y=True
        print("Called1234")
        try:
            if float(column[13]):
                pass
        except:
            return HttpResponse("enter float ") 
        myibj=POJ.objects.create(date=temp_date,
        company_name_id=f.company_name.id,
        location_id=f.location.id,
        jewellery_id=f.jewellery.id,
        center_stone_id=f.center_stone.id,
        color_of_center_stone_id=f.color_of_center_stone.id,
        shape_id=f.shape.id,
        metal_id=f.metal.id,
        grosswt=column[9],
        phone_number=column[10],
        cert_id=f.cert.id,
        pcs=column[12],
        amount=float(column[13]),
        discount_amount=float(column[15]),
        discount=float(z[0]),
        total=float(column[16]),
        purchase_approval=y,
        currencyid_id=f.currencyid.id,
        tag_price=float(column[18]),
        rate=float(column[19]),
        )
    return HttpResponse('Hi')
