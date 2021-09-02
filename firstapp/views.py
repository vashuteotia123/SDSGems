from django.views.generic import View
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.regex_helper import Group
from .models import *
from .forms import *
from django.urls import reverse_lazy

from shapeshifter.views import MultiFormView

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

# def showinvj(request):
#     invjobj=Inventoryofjewellery.objects.all()
#     context={
#         "showinvj":invjobj,
#     }
#     return render(request,"showinvj.html",context=context)


def showinv_d(request):
    if request.session:
        inv_dobj = Inventoryofdiamond.objects.all()
        context = {
            "showinv_d": inv_dobj,
        }
        return render(request, "showinvd.html", context=context)
    else:
        return render(request, "showinvd.html", {})


def showinv_cs(request):
    inv_csobj = Inventoryofcolorstones.objects.all()
    context = {
        "showinv_cs": inv_csobj,
    }
    return render(request, "showinvcs.html", context=context)


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


def returninv_d(request, id1):
    now = Inventoryofdiamond.objects.get(id=id1)
    # item = returnid(request, id1)
    context = {
        'returndiamond': now,
    }
    now.delete()

    return render(request, 'return_d.html', context=context)


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


form_list = []
class Cart(View):
    def get(self, request):
        print("called")
        total = cloneInvofjewellery.objects.all()
        for i in total:
            form_list.append(ADCForm(instance=i))

        # for item in form_list:
        #     print(item)
        context = {
            "totalitems": form_list,
        }
        return render(request, "showcart.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            print("hello m")
            for i in form_list:
                i=ADCForm(request.POST)
                if (i.is_valid()):
                    print("hello 2")
                    i.save()
        context = {
            "totalitems": form_list,
        }
        return render(request, "showcart.html", context=context)



# def show_jewwl_cart(request):
#         print("called")
#         total = cloneInvofjewellery.objects.all()
#         global form_list
#         form_list = []
#         for i in total:
#             form_list.append(ADCForm(instance=i))

#         for item in form_list:
#             print(item)
#             return render(request, "showcart.html")
#         context = {
#             "totalitems": form_list,
#         }
#         return render(request, "showcart.html", context=context)

#  def save_jewel_cart_form(request):
#      if()
#     return render(request, "showcart.html", context=context)