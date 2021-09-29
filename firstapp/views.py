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
    current.delete()
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
        allproduct = Inventoryofjewellery.objects.all()
        allclonej = cloneInvofjewellery.objects.all()
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
        j_obj.cartstatus = True
        j_obj.save()
        print(j_obj.cartstatus)
        new_object = cloneInvofjewellery.objects.create(stockid=j_obj.stockid, location=j_obj.location, jewellery_type=j_obj.jewellery_type, center_stone=j_obj.center_stone,
                                                        shape=j_obj.shape, metal=j_obj.metal, gross_wt=j_obj.grosswt, certificate=j_obj.cert,
                                                        PCS=j_obj.pcs, tag_price=j_obj.tag_price)
        return redirect('/delete')

    # def returnj(self, id):
    #     jobj = Inventoryofjewellery.objects.get(id=id)
    #     jobj.appvreturnstatus = True
    #     jobj.save()
    #     return redirect('/search')


# class Cart(View):
#     def showcart(self,request):
#         form_list = []
#         total = cloneInvofjewellery.objects.all()
#         for i in total:
#             form_list.append(ADCForm(instance=i))
#         if request.method == 'POST':
#             print("Function executed")
#             for item in form_list:
#                 print(item.location)
#                 # item.save()
#             return render(request, "showcart.html")

#         context = {
#         "totalitems": form_list,
#         }
#         # print(form_list)
#         return render(request, "showcart.html", context=context)

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
    Inventoryofjewellery.objects.create(stockid=object.stockid, )
    Salesofjewellery.objects.filter(pk=id).delete()
    context = {
        "productsj": Inventoryofjewellery.objects.all(),

    }
    return render(request, "showcart.html", context=context)

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


def deleteid_cs(request, idno):
    current = PurchaseOfColorStones.objects.get(id=idno)
    current.delete()
    return render(request, "delete.html")

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

def search_cs(request):
    print("Hello")
    posts = Inventoryofcolorstones.objects.all()
    search_term = ''
    search_term= request.POST.get('search_cs')
    posts = posts.filter(Q(location_icontains=search_item) | Q(id_icontains=search_item))
    context = {
            "product_cs":posts,
        }
    return render (request, " showinvcs.html", context=context)

def saving_colorstone_cart(request):
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
    object = Salesofcolorstones.objects.get(pk = id)
    Inventoryofcolorstones.objects.create(stockid=object.stockid, )
    Salesofcolorstones.objects.filter(pk=id).delete()
    context = {
        "products_cs": Inventoryofcolorstones.objects.all(),

    }
    return render(request, "showcart_cs.html", context=context)

def save_colorstones_forms(request):

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
        allproduct = Inventoryofcolorstones.objects.all()
        allclone_cs = cloneInvofcolorstones.objects.all()
        context = {
            "products_cs": allproduct,

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
        j_obj.cartstatus = True
        j_obj.save()
        print(j_obj.cartstatus)
        new_object = cloneInvofcolorstones.objects.create(stockid=j_obj.stockid, location=j_obj.location,shape=j_obj.shape, gem_type=j_obj.gem_type,
        origin=j_obj.origin,treatment=j_obj.treatment, certificate_no_cs=j_obj. certificate_no_cs,
        color=j_obj.color,measurements=j_obj.measurements,lab=j_obj.lab,PCS=j_obj.PCS,Weight_cs=j_obj.Weight_cs,tag_price_cs=j_obj.tag_price_cs)
        return redirect('/delete_cs')


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
    current.delete()
    return render(request, "delete.html")

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

def search_d(request):
    print("hello")
    posts =  Inventoryofdiamond.objects.all()
    search_term = ''
    search_term = request.POST.get('search_d')
    posts = posts.filter(Q(location_icontains=search_item) | Q(id_icontains=search_item))
    context = {
        "product_d": posts,
    }
    return render(request , " showinvd.html",context = context)

class Diamond_view(View):
    def get(self,request):
        print("hello")
        allproduct = Inventoryofdiamond.objects.all()
        allclone_d = cloneInvofdiamond.objects.all()
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
    Inventoryofdiamond.objects.create(stockid=object.stockid, )
    Salesofdiamond.objects.filter(pk=id).delete()
    context = {
        "products_d": Inventoryofdiamond.objects.all(),

    }
    return render(request, "showcart_d.html", context=context)
