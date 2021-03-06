from django.contrib.messages.api import MessageFailure
from django.core import paginator
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
import csv
import io
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from SDSDiamonds import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
import datetime

# Create your views here.


@login_required
def index(request):
    cscolors = colorofcstone.objects.all()
    context = {
        'cscolor': cscolors,
    }
    return render(request, 'index.html', context=context)


@login_required
def showform(request):
    latest = POJ.objects.last()
    form = POJForm(request.POST, initial={'stockid': latest.id})
    # countone=POJ.objects.all().count()
    if(form.is_valid()):
        form.save()
        return render(request, "index.html")
    context = {
        "formshow": form,
        "latest": POJ.objects.last()
    }
    return render(request, "form.html", context=context)


# def load_currency(request):
#     country_id = request.POST.get("country_id")
#     currency = currencies.objects.filter(country_id=country_id).all()
#     return render(request, 'templates/currency_dropdown_list_options.html', {'currency' : currency})

#  Jewellary Function


@login_required
def deleteid(request, idno):
    current = POJ.objects.get(id=idno)
    jstr = "J-"+str(idno)
    current_invj = Inventoryofjewellery.objects.get(stockid=jstr)
    current.delete()
    current_invj.delete()
    cloneInvofjewellery.objects.filter(stockid=jstr).delete()
    return redirect('/showj')


@login_required
def returnid(request, idno):
    current = POJ.objects.all()
    context = {
        "returnjewel": current,
    }
    return render(request, "returnj.html", context=context)


@login_required
def updateJ(request, pk):

    jewel_obj = POJ.objects.get(id=pk)
    form3 = POJForm(instance=jewel_obj)
    change_css = False
    browser_type = request.user_agent.browser.family
    if (browser_type == 'Edge' or browser_type == 'Chrome' or browser_type == 'Brave'):
        change_css = True
    if request.method == 'POST':
        form3 = POJForm(request.POST, instance=jewel_obj)
        if(form3.is_valid()):
            form3.save()
            cloneInvofjewellery.objects.filter(
                stockid=str("J-")+str(pk)).delete()
            messages.success(
                request, "Stock ID->{} is Modified  Successfully".format(str("J-")+str(pk)))
            return redirect('/showj')

    context = {'form3': form3, "b_s_c": change_css,
               "update_type": "Jewellery"+str(" Stock ID  J-")+str(pk), }
    return render(request, 'update_jewellery.html', context)


@login_required
def showjewell(request):
    objjewell = POJ.objects.all()
    invobj = list(Inventoryofjewellery.objects.values_list(
        'stockid', flat=True))
    invobjects_jewellery = []
    for i in invobj:
        z = i.replace("J-", "")
        invobjects_jewellery.append(int(z))
    if len(objjewell) <= 6:
        change = True
    else:
        change = False
    context = {
        "invobjects_jewellery": invobjects_jewellery,
        "showjewellery": objjewell,
        "css_adjust": change,
        "table_type": "Purchase Records of Jewellery",
    }
    return render(request, "showj.html", context=context)

# def delete(request, idno):
#     query = Inventoryofjewellery.objects.get(pk=idno)
#     query.delete()
#     return HttpResponse("Deleted!")


@login_required
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


# @login_required
# def returninvj(request, id):
#     now = Inventoryofjewellery.objects.get(id=id)
#     if now.appvreturnstatus is False:
#         now.appvreturnstatus==True
#     return redirect("/index")


@login_required
def retobj_j(request):
    objectsj = Inventoryofjewellery.objects.filter(appvreturnstatus=True)
    context = {
        "returned": objectsj,
    }
    return render(request, "returnj.html", context=context)


@login_required
def returninv_cs(request, id1):
    now = Inventoryofcolorstones.objects.get(id=id1)
    # item = returnid(request, id1)
    context = {
        'returncs': now,
    }
    now.delete()

    return render(request, 'return_cs.html', context=context)

# @login_required
# def search(request):
#     posts = Inventoryofjewellery.objects.all()
#     search_term = ''
#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         posts = posts.filter(Q(id__icontains=search_term) | Q(jewellery_type__icontains=search_term))
#         context={
#             "showvalue":posts,

#         }
#         return render(request,"search.html",context=context)
#     else:
#         return render(request,".html",{})


# @login_required
# def addjtocart(request, primkey):

#     j_obj = Inventoryofjewellery.objects.get(id=primkey)
#     new_object = cloneInvofjewellery.objects.create(stockid=j_obj.stockid, location=j_obj.location, jewellery_type=j_obj.jewellery_type, center_stone=j_obj.center_stone,
#                                                     shape=j_obj.shape, metal=j_obj.metal, gross_wt=j_obj.grosswt, certificate=j_obj.cert,
#                                                     PCS=j_obj.pcs, tag_price=j_obj.tag_price)
#     return redirect('/showinvj')


# @login_required
# def showcart(request):
#     total = cloneInvofjewellery.objects.all()
#     global formlist
#     form_list = []
#     for i in total:
#         form_list.append(ADCForm(instance=i))
#     if request.method == "POST":

#         for item in form_list:
#         return render(request, "showcart.html")
#     context = {
#         "totalitems": form_list,
#     }
#     return render(request, "showcart.html", context=context)


@login_required
def search(request):
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
    method_decorator(login_required)

    def get(self, request):
        z = []
        y = list()
        jewel_types = set(
            Inventoryofjewellery.objects.values_list('stockid', flat=True))
        for sentence in jewel_types:
            sentence = sentence.replace("J-", "")
            z.append(int(sentence))
        z.sort()
        z = map(str, z)
        for i in z:
            i = "J-"+i
            y.append(i)
        allproduct = []
        for j in y:
            product = Inventoryofjewellery.objects.get(stockid=j)
            allproduct.append(product)

        length_jewel = Inventoryofjewellery.objects.all().count()
        if length_jewel <= 6:
            change = True
        else:
            change = False
        context = {
            "productsj": allproduct,
            "length_jewel": length_jewel,
            "css_adjust": change,
            "table_type": "Inventory of Jewellery",
        }
        return render(request, "showinvj.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            jewell_ids = request.POST.getlist('id[]')
            for id in jewell_ids:
                j = Inventoryofjewellery.objects.get(id=id)
                j.cartstatus = False
                j.frontend = False
                cloneInvofjewellery.objects.filter(stockid=j.stockid).delete()
                j.appvreturnstatus = True
                j.save()
        return redirect('delete-jewell')

    def addtocart(self, id):
        j_obj = Inventoryofjewellery.objects.get(id=id)
        z = j_obj.stockid
        x = re.findall("[0-9]+", z)
        idj = int(x[0])
        j_obj2 = POJ.objects.filter(id=idj)
        j_obj3 = POJ.objects.get(id=idj)
        j_obj.cartstatus = True
        j_obj.save()
        new_object = cloneInvofjewellery.objects.create(stockid=j_obj.stockid, location=j_obj.location, jewellery_type=j_obj.jewellery_type, center_stone=j_obj.center_stone,
                                                        color_of_center_stone=j_obj.color_of_center_stone, shape=j_obj.shape, metal=j_obj.metal,
                                                        center_stone_weight=j_obj.center_stone_weight,
                                                        center_stone_pieces=j_obj.center_stone_pieces,
                                                        gross_wt=j_obj.grosswt, certificate=j_obj.cert,
                                                        PCS=j_obj.pcs, tag_price=j_obj.tag_price)
        if j_obj.purchaseapv is False:
            j_obj2.update(purchase_approval=True)
        return redirect('delete-jewell')


def allselljewellrecords(request):
    sold_items = Salesofjewellery.objects.all()
    if len(sold_items) <= 6:
        change = True
    else:
        change = False
    context = {
        "sold_items": Salesofjewellery.objects.all(),
        "css_adjust": change,
        "table_type": "Sales Record of Jewellery ",
    }
    return render(request, "show_sell_jewel_table.html", context=context)


@login_required
def backtoinv(request, id):
    myobj = Inventoryofjewellery.objects.get(id=id)
    myobj.appvreturnstatus = False
    myobj.cartstatus = False
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


@login_required
def saving_jewel_cart(request):
    total = cloneInvofjewellery.objects.all()
    if len(total) <= 6:
        initial_change = False
        change = True
    else:
        initial_change = True
        change = False
    total_jewels = list(total.values())
    jewel_formset = ADCFormSet(initial=total_jewels)
    if request.method == "POST":
        curr_formset = ADCFormSet(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
            context = {
                "totalitems": curr_formset,
                'itemcount': len(curr_formset),
                "is_valid": True,
                "css_adjust_displaycart2_cs": change,
                "displaycart2_cs": initial_change,
                "css_adjust": change,
                "table_type": "Jewellery Cart", }
            return render(request, "showcart.html", context=context)
        else:
            context = {
                "totalitems": curr_formset,
                'itemcount': len(curr_formset),
                "is_valid": False,
                "css_adjust_displaycart2_cs": change,
                "displaycart2_cs": initial_change,
                "css_adjust": change,
                "table_type": "Jewellery Cart", }
            return render(request, "showcart.html", context=context)
    context = {

        "totalitems": jewel_formset,
        'itemcount': len(total),
        "css_adjust_displaycart2_cs": change,
        "displaycart2_cs": initial_change,
        "css_adjust": change,
        "table_type": "Jewellery Cart",
    }
    return render(request, "showcart.html", context=context)


@login_required
def sell_jewel(request):
    jewellery_objects = cloneInvofjewellery.objects.all()

    try:
        for object in jewellery_objects:
            Salesofjewellery.objects.create(
                date=object.date,
                stockid=object.stockid,
                company_name=object.company_name,
                location=object.location,
                jewellery_type=object.jewellery_type,
                center_stone=object.center_stone,
                color_of_center_stone=object.color_of_center_stone,
                shape=object.shape,
                metal=object.metal,
                center_stone_weight=object.center_stone_weight,
                center_stone_pieces=object.center_stone_pieces,
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

            Inventoryofjewellery.objects.filter(
                stockid=object.stockid).delete()
            cloneInvofjewellery.objects.filter(stockid=object.stockid).delete()
        if len(jewellery_objects) <= 6:
            change = True
        else:
            change = False
        context = {
            "sold_items": Salesofjewellery.objects.all(),
            "css_adjust": change,
            "table_type": "Sales Records of Jewellery",


        }
        return render(request, "show_sell_jewel_table.html", context=context)
    except:
        total = cloneInvofjewellery.objects.all()
        total_jewels = list(total.values())
        jewel_formset = ADCFormSet(initial=total_jewels)
        if request.method == "POST":
            curr_formset = ADCFormSet(data=request.POST)
            if(curr_formset.is_valid()):
                curr_formset.save()
        context = {
            "totalitems": jewel_formset,
            "message": "Fill out all the fields before performing sell action."
        }
        return render(request, "showcart.html", context=context)


@ login_required
def return_jewel_Inventory(request, id):
    object = Salesofjewellery.objects.get(pk=id)
    Inventoryofjewellery.objects.create(stockid=object.stockid,

                                        location=object.location,
                                        jewellery_type=object.jewellery_type,
                                        center_stone=object.center_stone,
                                        color_of_center_stone=object.color_of_center_stone,
                                        shape=object.shape,
                                        metal=object.metal,
                                        grosswt=object.gross_wt,
                                        center_stone_weight=object.center_stone_weight,
                                        center_stone_pieces=object.center_stone_pieces,
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
        grosswt=object.gross_wt,
        jewellery_type=object.jewellery_type,
        total_amount=object.total_value,
        currency=object.currency,
    )
    Salesofjewellery.objects.filter(pk=id).delete()
    return redirect('delete-jewell')


@login_required
def save_jewel_forms(request):

    poj_formset = POJFormSet(queryset=POJ.objects.none())
    if request.method == "POST":
        curr_formset = POJFormSet(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems": poj_formset,
        "table_type": "Purchase of Jewellery"
    }
    return render(request, "show_jewel_form.html", context=context)


def PurchaseofJewelleryFormCount(request):
    return render(request, 'PurchaseofJewelleryFormCount.html')


class BirdAddView(TemplateView):
    template_name = "show_jewel_form.html"

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        # formset = POJFormSet(queryset=POJ.objects.none(),)
        form_count = self.request.GET.get('form_count')
        try:
            form_count = int(form_count)
        except:
            pass
        if form_count == 0:
            messages.error(
                self.request, "Zero forms cannot be greated due to your IQ.")
            return redirect(self.request.META.get('HTTP_REFERER'))
        if form_count is None:
            return redirect('/PurchaseofJewelleryFormCount')
        form_count = int(form_count)
        formset_factory = modelformset_factory(POJ, POJForm, extra=form_count)
        formset = formset_factory(queryset=POJ.objects.none(), )

        return self.render_to_response({'totalitems': formset, "table_type": "Purchase Form of Jewellery", "total": len(formset)})

    # @login_required
# define method to handle POST request

    def post(self, *args, **kwargs):

        formset = POJFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            for i in range(len(formset)):
                if formset[i].cleaned_data == {}:
                    messages.error(self.request, "Please fill up the form.")
                    return self.render_to_response({'totalitems': formset})
            formset.save()
            messages.success(self.request, "Forms saved successfully!")
            return redirect("/showj")

        return self.render_to_response({'totalitems': formset})


@login_required
def displaysalesreturn(request):
    ret_sj = Salesreturn.objects.all()
    context = {
        "ret_sj": ret_sj,
    }
    return render(request, "salereturnjewellery.html", context=context)


@login_required
def displaycart2(request):
    tjcart = cloneInvofjewellery.objects.all()
    if len(tjcart) <= 6:
        initial_change = False
        change = True
    else:
        initial_change = True
        change = False
    context = {
        "css_adjust_displaycart2_cs": change,
        "displaycart2_cs": initial_change,
        "tjcart": tjcart,
        "table_type": "Jewellery Cart",
    }
    return render(request, "displaycart.html", context=context)


@login_required
def return_jewel_cart(request, id):
    rjc = cloneInvofjewellery.objects.get(id=id)
    rjc2 = Inventoryofjewellery.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv is False:
        x = re.findall("[0-9]+", rjc2.stockid)
        rdj = int(x[0])
        xy = POJ.objects.filter(id=rdj)
        xy.update(purchase_approval=False)
    rjc2.cartstatus = False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2')


# Color stones function

@login_required
def showcs(request):
    cs_obj = PurchaseOfColorStones.objects.all()
    invobj = list(Inventoryofcolorstones.objects.values_list(
        'stockid', flat=True))
    invobjectscs = []
    for i in invobj:
        z = i.replace("C-", "")
        invobjectscs.append(int(z))
    if len(cs_obj) <= 6:
        change = True
    else:
        change = False
    context = {
        "show_cs": cs_obj,
        "invobjectscs": invobjectscs,
        "css_adjust": change,
        "table_type": "Purchase Records of Colourstone",
    }
    return render(request, "showcs.html", context=context)


@login_required
def returnid_cs(request, idno):
    current = PurchaseOfColorStones.objects.all()
    context = {
        "returncs": current,
    }
    return render(request, "return_cs.html", context=context)


@login_required
def update_cs(request, ck):

    cs_obj = PurchaseOfColorStones.objects.get(id=ck)
    form5 = POCSForm(instance=cs_obj)
    change_css = False
    browser_type = request.user_agent.browser.family
    if (browser_type == 'Edge' or browser_type == 'Chrome' or browser_type == 'Brave'):
        change_css = True
    if request.method == 'POST':
        form5 = POCSForm(request.POST, instance=cs_obj)
        if(form5.is_valid()):
            form5.save()
            cloneInvofcolorstones.objects.filter(
                stockid=str("C-")+str(ck)).delete()
            messages.success(
                request, "Stock ID->{} is Modified  Successfully".format(str("C-")+str(ck)))
            return redirect('/showcs')

    context = {'form5': form5, "b_s_c": change_css,
               "update_type": "Colourstone Stock ID C-"+str(ck)}
    return render(request, 'update_cs.html', context)


# @login_required
# def deleteid_cs(request, idno):
#     current = PurchaseOfColorStones.objects.get(id=idno)
#     current.delete()
#     return render(request, "delete.html")


@login_required
def deleteid_cs(request, idno):

    current = PurchaseOfColorStones.objects.get(id=idno)
    c_str = "C-"+str(idno)
    try:
        current_invcs = Inventoryofcolorstones.objects.get(stockid=c_str)
        current_invcs.delete()
    except:
        messages.success(request, "Data record not found in Inventory!")
        return redirect(request.META.get('HTTP_REFERER'))
    current.delete()
    cloneInvofcolorstones.objects.filter(stockid=c_str).delete()
    messages.success(request, "Deleted Successfully")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def showinv_cs(request):
    inv_csobj = Inventoryofcolorstones.objects.all()

    context = {
        "showinv_cs": inv_csobj,
    }
    return render(request, "showinvcs.html", context=context)


@login_required
def retobj_cs(request):
    object_cs = Inventoryofcolorstones.objects.filter(appvreturnstatus=True)
    context = {
        "returned_cs": object_cs,
    }
    return render(request, "return_cs.html", context=context)


@login_required
def backtoinvcs1(request, id):
    myobj = Inventoryofcolorstones.objects.get(id=id)
    myobj.appvreturnstatus = False
    myobj.cartstatus = False
    myobj.save()
    totalobjs = Inventoryofcolorstones.objects.filter(
        appvreturnstatus=True)
    return redirect('/retobj_cs')


@login_required
def saving_colorstone_cart(request):
    total = cloneInvofcolorstones.objects.all()
    total_colorstones = list(total.values())
    colorstone_formset = ADCFormSet_cs(initial=total_colorstones)
    if len(total) <= 6:
        change = True
    else:
        change = False
    if request.method == "POST":
        curr_formset = ADCFormSet_cs(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
            return render(request, 'showcart_cs.html', {"totalitems_cs": curr_formset, "table_type": "Cart Items", "css_adjust": change, 'is_valid': True, 'itemcount': len(curr_formset)})
        else:
            context = {"totalitems_cs": curr_formset, "css_adjust": change,
                       "table_type": "Cart Items", 'is_valid': False, 'itemcount': len(curr_formset)}
            return render(request, 'showcart_cs.html', context)
    context = {
        "totalitems_cs": colorstone_formset,
        "table_type": "Cart Items",
        "css_adjust": change,
        'itemcount': len(total),
    }
    return render(request, "showcart_cs.html", context=context)


@login_required
def sell_cs(request):
    cs_objects = cloneInvofcolorstones.objects.all()

    for object in cs_objects:
        Salesofcolorstones.objects.create(
            date=object.date,
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
            price=object.price,
            units_cs=object.units_cs,
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
    if len(cs_objects) <= 6:
        change = True
    else:
        change = False
    context = {
        "sold_items": Salesofcolorstones.objects.all(),
        "css_adjust": change,
        "table_type": "Sales Records of Colourstone",
    }
    return render(request, "show_sell_cs_table.html", context=context)


@login_required
def allsellcsrecords(request):
    sold_items = Salesofcolorstones.objects.all()
    if len(sold_items) <= 6:
        change = True
    else:
        change = False
    context = {
        "sold_items": Salesofcolorstones.objects.all(),
        "css_adjust": change,
        "table_type": "Sales Record of Colourstone",
    }
    return render(request, "show_sell_cs_table.html", context=context)
    # except:
    #     messages.success(request, 'Please fill all the details')
    #     return redirect('show_colorstone_cart')


@login_required
def return_colorstone_Inventory(request, id):
    object = Salesofcolorstones.objects.get(id=id)
    Inventoryofcolorstones.objects.create(
        stockid=object.stockid,
        shape=object.shape,
        location=object.location,
        gem_type=object.gem_type,
        origin=object.origin,
        treatment=object.treatment,
        certificate_no=object.certificate_no,
        PCS=object.PCS,
        Clarity=object.Clarity,
        lab=object.lab,
        color=object.color,
        units=object.units_cs,
        purchaseapv=True,
        Weight=object.Weight_cs,
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
        weight=object.Weight_cs,
        clarity=object.Clarity,
        total_amount=object.total_value_cs,
        colour=object.color,
        price=object.price,
        currency=object.currency_cs,


    )
    Salesofcolorstones.objects.filter(pk=id).delete()
    return redirect('delete-cs')


@login_required
def save_colorstone_forms(request):
    pocs_formset = POCSFormSet(queryset=PurchaseOfColorStones.objects.none())
    if request.method == "POST":
        curr_formset = POCSFormSet(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()

    context = {
        "totalitems_cs": pocs_formset,
    }
    return render(request, "show_colorstone_form.html", context=context)


def purchaseOfColorStoneFormCount(request):
    return render(request, "purchaseOfColorStoneFormCount.html")


class CSAddView(TemplateView):

    template_name = "show_colorstone_form.html"

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        form_count = self.request.GET.get('form_count')
        try:
            form_count = int(form_count)
        except:
            pass
        if form_count == 0:
            messages.error(
                self.request, "Zero forms cannot be greated due to your IQ.")
            return redirect(self.request.META.get('HTTP_REFERER'))
        if form_count is None:
            return redirect('/purchaseOfColorStoneFormCount')
        form_count = int(form_count)
        formset_factory = modelformset_factory(
            PurchaseOfColorStones, POCSForm, extra=form_count)
        formset = formset_factory(
            queryset=PurchaseOfColorStones.objects.none(), )
        return self.render_to_response({'totalitems_cs': formset, "table_type": "Purchase Form of Colourstone", "total": len(formset)})

    def post(self, request, *args, **kwargs):

        formset = POCSFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            if formset[0].cleaned_data == {}:
                messages.error(request, "Please fill up the form.")
                return self.render_to_response({'totalitems_cs': formset})
            formset.save()
            return redirect("/index")

        return self.render_to_response({'totalitems_cs': formset})


class colorstone_view(View):
    @method_decorator(login_required)
    def get(self, request):
        z = []
        y = list()
        jewel_types = set(
            Inventoryofcolorstones.objects.values_list('stockid', flat=True))
        for sentence in jewel_types:
            sentence = sentence.replace("C-", "")
            z.append(int(sentence))
        z.sort()
        z = map(str, z)
        for i in z:
            i = "C-"+i
            y.append(i)
        allproduct = []
        for j in y:
            product = Inventoryofcolorstones.objects.get(stockid=j)
            allproduct.append(product)
        product_cs = Inventoryofcolorstones.objects.all()
        if len(product_cs) <= 6:
            change = True
        else:
            change = False
        length_cs = len(allproduct)
        context = {"products_cs": allproduct, "css_adjust": change,
                   "table_type": "Inventory of Colourstone", "length_cs": length_cs}
        return render(request, "showinvcs.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            cs_ids = request.POST.getlist('id[]')
            for id in cs_ids:
                j = Inventoryofcolorstones.objects.get(id=id)
                cloneInvofjewellery.objects.filter(stockid=j.stockid).delete()
                j.cartstatus = False
                j.appvreturnstatus = True
                j.frontend = False
                j.save()
        return redirect('delete-cs')

    def addtocart_cs(self, id):
        j_obj = Inventoryofcolorstones.objects.get(id=id)
        z = j_obj.stockid
        x = re.findall("[0-9]+", z)
        idcs = int(x[0])
        j_obj2 = PurchaseOfColorStones.objects.filter(id=idcs)
        j_obj3 = PurchaseOfColorStones.objects.get(id=idcs)
        j_obj.cartstatus = True
        j_obj.save()
        new_object = cloneInvofcolorstones.objects.create(stockid=j_obj.stockid, location=j_obj.location, shape=j_obj.shape, gem_type=j_obj.gem_type,
                                                          origin=j_obj.origin, treatment=j_obj.treatment, certificate_no=j_obj. certificate_no,
                                                          color=j_obj.color, measurements=j_obj.measurements, lab=j_obj.lab, PCS=j_obj.PCS,
                                                          Weight_cs=j_obj.Weight, Clarity=j_obj.Clarity,
                                                          tag_price_cs=j_obj.tag_price, units_cs=j_obj.units)
        if j_obj.purchaseapv is False:
            j_obj2.update(purchaseapv=True)
        return redirect('/inventory_color_stone')

#  extra function cs


@login_required
def returncart2_cs(request, id):
    myobject = cloneInvofcolorstones.objects.get(id=id)
    invobj = Inventoryofcolorstones.objects.get(stockid=myobject.stockid)
    invobj.cartstatus = False
    invobj.save()
    tcscart = cloneInvofcolorstones.objects.all()
    context = {
        "tcscart": tcscart,
    }
    return render(request, "displaycart_cs.html", context=context)


@login_required
def displaysalesreturn_cs(request):
    ret_scs = Salesreturn_cs.objects.all()
    context = {
        "ret_scs": ret_scs,
    }
    return render(request, "salereturncolorstones.html", context=context)


@login_required
def displaycart2_cs(request):
    tcscart = cloneInvofcolorstones.objects.all()
    if len(tcscart) <= 6:
        initial_change = False
        change = True
    else:
        initial_change = True
        change = False
    context = {
        "css_adjust_displaycart2_cs": change,
        "displaycart2_cs": initial_change,
        "table_type": "Cart",
        "tcscart": tcscart,
    }
    return render(request, "displaycart_cs.html", context=context)


@login_required
def return_colorstone_cart(request, id):
    rjc = cloneInvofcolorstones.objects.get(id=id)
    rjc2 = Inventoryofcolorstones.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv is False:
        x = re.findall("[0-9]+", rjc2.stockid)
        rdj = int(x[0])
        xy = PurchaseOfColorStones.objects.filter(id=rdj)
        xy.update(purchaseapv=False)
    rjc2.cartstatus = False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2_cs')

# Diamond Function


@login_required
def showdiamond(request):
    diamondobj = POD.objects.all()
    invobj = list(Inventoryofdiamond.objects.values_list(
        'stockid', flat=True))
    if len(diamondobj) < 8:
        change = True
    else:
        change = False
    invobjects_diamonds = []
    for i in invobj:
        z = i.replace("D-", "")
        invobjects_diamonds.append(int(z))
    context = {
        "invobjects_diamonds": invobjects_diamonds,
        "showdia": diamondobj,
        "table_type": "Purchase Records of Diamonds",
        "css_adjust": change
    }
    return render(request, "showd.html", context=context)


@login_required
def update_d(request, dk):

    diamond_obj = POD.objects.get(id=dk)
    form4 = PODForm(instance=diamond_obj)
    change_css = False
    browser_type = request.user_agent.browser.family
    if (browser_type == 'Edge' or browser_type == 'Chrome' or browser_type == 'Brave'):
        change_css = True
    if request.method == 'POST':
        form4 = PODForm(request.POST, instance=diamond_obj)
        if(form4.is_valid()):
            form4.save()
            cloneInvofdiamond.objects.filter(
                stockid=str("D-")+str(dk)).delete()
            messages.success(
                request, "Stock ID->{} is Modified  Successfully".format(str("D-")+str(dk)))
            return redirect('/showd')

    context = {'form4': form4, "b_s_c": change_css,
               "update_type": "Diamonds Stock ID D-"+str(dk)}
    return render(request, 'update_diamond.html', context)


@login_required
def returnid_d(request, idno):
    current = POD.objects.all()
    context = {
        "returndiamond": current,
    }
    return render(request, "return_d.html", context=context)


@login_required
def deleteid_d(request, idno):
    current = POD.objects.get(id=idno)
    d_str = "D-"+str(idno)
    current_invd = Inventoryofdiamond.objects.get(stockid=d_str)
    current.delete()
    current_invd.delete()
    cloneInvofdiamond.objects.filter(stockid=d_str).delete()
    messages.success(request, d_str + " Deleted Successfully")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def showinv_d(request):
    if request.session:
        inv_dobj = Inventoryofdiamond.objects.all()
        context = {
            "showinv_d": inv_dobj,
        }
        return render(request, "showinvd.html", context=context)


@login_required
def returninv_d(request, id1):
    now = Inventoryofdiamond.objects.get(id=id1)
    # item = returnid(request, id1)
    context = {
        'returndiamond': now,
    }
    now.delete()

    return render(request, 'return_d.html', context=context)


@login_required
def saving_diamond_cart(request):
    total = cloneInvofdiamond.objects.all()
    total_diamond = list(total.values())
    diamond_formset = ADCFormSet_d(initial=total_diamond)
    if(len(total) <= 7):
        change = True
    else:
        change = False
    if request.method == "POST":
        curr_formset = ADCFormSet_d(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
            context = {
                "totalitems_d": curr_formset,
                "itemcount": len(curr_formset),
                "is_valid": True,
                "table_type": "Cart Items",
                "css_adjust": change,
            }
            return render(request, "showcart_d.html", context=context)
        else:
            context = {
                "itemcount": len(curr_formset),
                "totalitems_d": curr_formset,
                "table_type": "Cart Items",
                "css_adjust": change,
            }
            return render(request, "showcart_d.html", context=context)
    context = {
        "totalitems_d": diamond_formset,
        "itemcount": len(total),
        "table_type": "Cart Items",
        "css_adjust": change,
    }
    return render(request, "showcart_d.html", context=context)


@login_required
def save_diamond_forms(request):

    pod_formset = PODFormSet(queryset=POD.objects.none())
    if request.method == "POST":
        curr_formset = PODFormSet(data=request.POST)
        if(curr_formset.is_valid()):
            curr_formset.save()
    context = {
        "totalitems_d": pod_formset,
    }
    return render(request, "show_diamond_form.html", context=context)


def purchaseOfDiamondFormCount(request):
    return render(request, "purchaseOfDiamondFormCount.html")


class DiamondAddView(TemplateView):
    template_name = "show_diamond_form.html"

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        form_count = self.request.GET.get('form_count')
        try:
            form_count = int(form_count)
        except:
            pass
        if form_count == 0:
            messages.error(
                self.request, "Zero forms cannot be greated due to your IQ.")
            return redirect(self.request.META.get('HTTP_REFERER'))
        if form_count is None:
            return redirect('/purchaseOfDiamondFormCount')
        form_count = int(form_count)
        formset_factory = modelformset_factory(POD, PODForm, extra=form_count)
        formset = formset_factory(queryset=POD.objects.none(), )
        return self.render_to_response({'totalitems_d': formset, "table_type": "Purchase Form of Diamonds", "total": len(formset)})

    def post(self, *args, **kwargs):

        formset = PODFormSet(data=self.request.POST)
        if formset.is_valid():
            if formset[0].cleaned_data == {}:
                messages.error(self.request, "Please fill up the form.")
                return self.render_to_response({'totalitems_d': formset})
            formset.save()
            messages.success(self.request, "Forms saved successfully!")
            return redirect("/showd")

        return self.render_to_response({'totalitems_d': formset})


@login_required
def retobj_d(request):
    objects_d = Inventoryofdiamond.objects.filter(appvreturnstatus_d=True)
    context = {
        "returned_d": objects_d,
    }
    return render(request, "return_d.html", context=context)


class Diamond_view(View):
    @method_decorator(login_required)
    def get(self, request):
        z = []
        y = list()
        diamond_types = set(
            Inventoryofdiamond.objects.values_list('stockid', flat=True))
        for sentence in diamond_types:
            sentence = sentence.replace("D-", "")
            z.append(int(sentence))
        z.sort()
        z = map(str, z)
        for i in z:
            i = "D-"+i
            y.append(i)
        allproduct = []
        for j in y:
            product = Inventoryofdiamond.objects.get(stockid=j)
            allproduct.append(product)
        # allclone_d = cloneInvofdiamond.objects.all()
        length_diamond = Inventoryofdiamond.objects.filter(
            appvreturnstatus_d=False).count()
        if length_diamond <= 6:
            change = True
        else:
            change = False
        context = {
            "products_d": allproduct,
            "table_type": "Inventory of Diamonds",
            "css_adjust": change,
            "length_diamond": length_diamond,

        }
        return render(request, "showinvd.html", context=context)

    def post(self, request, *args, **kwargs):
        if(request.method == "POST"):
            d_ids = request.POST.getlist('id[]')
            for id in d_ids:
                j = Inventoryofdiamond.objects.get(id=id)
                j.appvreturnstatus_d = True
                j.cartstatus = False
                j.frontend = False
                cloneInvofdiamond.objects.filter(stockid=j.stockid).delete()
                j.save()
        return redirect('delete-d')

    def addtocart_d(self, id):
        j_obj = Inventoryofdiamond.objects.get(id=id)
        z = j_obj.stockid
        x = re.findall("[0-9]+", z)
        id_d = int(x[0])
        j_obj2 = POD.objects.filter(id=id_d)
        j_obj3 = POD.objects.get(id=id_d)
        j_obj.cartstatus = True
        j_obj.save()
        new_object = cloneInvofdiamond.objects.create(stockid=j_obj.stockid, location=j_obj.location, shape=j_obj.shape, clarity=j_obj.clarity,
                                                      white_color_grade1=j_obj.white_color_grade1, color_origin1=j_obj.color_origin1,  fancycolor_grade=j_obj.fancycolor_grade,
                                                      cut=j_obj.cut, polish=j_obj.polish, symmetry=j_obj.symmetry, measurements=j_obj.measurements, depth=j_obj.depth, table=j_obj.table,
                                                      fluorescence_intensity=j_obj.fluorescence_intensity, fluorescence_color=j_obj.fluorescence_color, certificate_no_d=j_obj. certificate_no_d, certificate_d=j_obj.certificate_d, laser_inscription=j_obj.laser_inscription, PCS_d=j_obj.PCS_d, weight_d=j_obj.weight_d, units=j_obj.units, tag_price_d=j_obj.tag_price_d)

        if j_obj.purchaseapv_d is False:
            j_obj2.update(purchaseapv_d=True)
        return redirect('/inventory_of_diamonds')


@login_required
def backtoinv_d(request, id):
    myobj = Inventoryofdiamond.objects.get(id=id)
    myobj.appvreturnstatus_d = False
    myobj.cartstatus = False
    myobj.save()
    totalobjs = Inventoryofdiamond.objects.filter(appvreturnstatus_d=True)
    return redirect('/retobj_d')


@login_required
def sell_diamond(request):
    diamond_objects = cloneInvofdiamond.objects.all()
    if len(diamond_objects) <= 6:
        change = True
    else:
        change = False
    for object in diamond_objects:
        Salesofdiamond.objects.create(
            date=object.date,
            stockid=object.stockid,
            company_name=object.company_name,
            location=object.location,
            shape=object.shape,
            clarity=object.clarity,
            color_origin1=object.color_origin1,
            white_color_grade1=object.white_color_grade1,
            # fancy_color_intensity1=object.fancy_color_intensity1,
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
            price=object.price,
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
        "sold_items": Salesofdiamond.objects.all(),
        "css_adjust": change,
        "table_type": "Sell Items",
    }
    return render(request, "show_sell_diamond_table.html", context=context)


def allselldiamondsrecords(request):
    if(Salesofdiamond.objects.all().count() <= 6):
        change = True
    else:
        change = False
    context = {
        "sold_items": Salesofdiamond.objects.all(),
        "css_adjust": change,
        "table_type": "Sales Records Of Diamonds",
    }
    return render(request, "show_sell_diamond_table.html", context=context)


@login_required
def return_diamond_Inventory(request, id):
    object = Salesofdiamond.objects.get(pk=id)
    Inventoryofdiamond.objects.create(stockid=object.stockid,
                                      #   fancy_color_intensity1=object.fancy_color_intensity1,
                                      location=object.location,
                                      shape=object.shape,
                                      clarity=object.clarity,
                                      white_color_grade1=object.white_color_grade1,
                                      fancycolor_grade=object.fancycolor_grade,
                                      certificate_no_d=object.certificate_no_d,
                                      PCS_d=object.PCS_d,
                                      purchaseapv_d=True,
                                      color_origin1=object.color_origin1,
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


                                      )
    Salesreturn_d.objects.create(
        company_name=object.company_name,
        weight=object.weight_d,
        clarity=object.clarity,
        colour=object.white_color_grade1.w_c_g+' , '+object.fancycolor_grade,
        stockid=object.stockid,
        location=object.location,
        shape=object.shape,
        totalamount=object.total_value_d,
        price=object.price,
        currency=object.currency,

    )
    Salesofdiamond.objects.filter(pk=id).delete()
    return redirect('/inventory_of_diamonds')


@login_required
def return_diamond_cart(request, id):
    rjc = cloneInvofdiamond.objects.get(id=id)
    rjc2 = Inventoryofdiamond.objects.get(stockid=rjc.stockid)
    if rjc2.purchaseapv_d is False:
        x = re.findall("[0-9]+", rjc2.stockid)
        rdj = int(x[0])
        xy = POD.objects.filter(id=rdj)
        xy.update(purchaseapv_d=False)
    rjc2.cartstatus = False
    rjc2.save()
    rjc.delete()
    return redirect('/displaycart2_d')


# extra function d

@login_required
def returncart2_d(request, id):
    myobject = cloneInvofdiamond.objects.get(id=id)
    invobj = Inventoryofdiamond.objects.get(stockid=myobject.stockid)
    invobj.cartstatus = False
    invobj.save()
    tdcart = cloneInvofdiamond.objects.all()
    context = {
        "tdcart": tdcart,
    }
    return render(request, "displaycart_d.html", context=context)


@login_required
def displaysalesreturn_d(request):
    ret_sd = Salesreturn_d.objects.all()
    context = {
        "ret_sd": ret_sd,
    }
    return render(request, "salereturndiamond.html", context=context)


@login_required
def displaycart2_d(request):
    tdcart = cloneInvofdiamond.objects.all()
    if len(tdcart) <= 6:
        initial_change = False
        change = True
    else:
        initial_change = True
        change = False
    context = {
        "css_adjust_displaycart2_cs": change,
        "displaycart2_cs": initial_change,
        "tdcart": tdcart,
        "table_type": "Diamond Cart",
    }
    return render(request, "displaycart_d.html", context=context)


@login_required
def jewellery_upload(request):
    template = "jewelleryupload.html"
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    column_names = str(next(io_string))
    counter = 1
    column_names = column_names.split(",")
    for column in csv.reader(io_string, delimiter=','):
        # datere=re.findall(r'\d{2}/\d{2}/\d{4}',column[0])
        # date_value=list(datere[0])
        # final_date=datetime.date(int(''.join(date_value[6:])),int(''.join(date_value[3:4])),int(''.join(date_value[0:2])))
        temp_date = datetime.datetime.strptime(
            str(column[0]), "%d-%m-%Y").date()
        f = clonePOJ
        for i in range(len(column)):
            if(i == 1 or i == 8 or i == 12):
                continue
            if(column[i] == ""):
                messages.error(request, "ERROR: {} cannot be empty for entry:  {}. Please remove all the entries from 1 to {} in the CSV file and try again.".format(
                    column_names[i], str(counter), str(counter-1)))
                return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.company_name = companyinfo.objects.get(
                company_name=column[2].lower())
        except ObjectDoesNotExist:
            messages.error(
                request, "Company Name -> {} does not exist, Add company from top bar!\n Also remove all the enteries prior to {}".format(column[2], str(counter - 1)))
            return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.location, lcobj = location.objects.get_or_create(
                place=column[3].lower())
            if lcobj:
                f.location.save()
        except Exception as e:
            raise e
        try:
            f.jewellery, jlobj = jewell.objects.get_or_create(
                jewel=column[4].lower())
            if jlobj:
                f.jewellery.save()
        except Exception as e:
            raise e
        try:
            f.center_stone, clobj = centerstone.objects.get_or_create(
                stone=column[5].lower())
            if clobj:
                f.center_stone.save()
        except Exception as e:
            raise e
        try:
            f.color_of_center_stone, clsobj = colorofcstone.objects.get_or_create(
                color=column[6].lower())
            if clsobj:
                f.color_of_center_stone.save()
        except Exception as e:
            raise e
        try:
            f.shape, sobj = shape1.objects.get_or_create(
                shape=column[7].lower())
            if sobj:
                f.shape.save()
        except Exception as e:
            raise e

        try:
            f.metal, mobj = metal1.objects.get_or_create(
                metal=column[8].lower())
            if mobj:
                f.metal.save()
        except Exception as e:
            raise e

        try:
            f.cert, cerobj = certificate.objects.get_or_create(
                cert=column[12].lower())
            if cerobj:
                f.cert.save()
        except Exception as e:
            raise e

        try:
            f.currency, crobj = currencies.objects.get_or_create(
                currency=column[18].lower())
            if crobj:
                f.currency.save()
        except Exception as e:
            raise e
        if(column[21].lower() == "no"):

            y = False
        else:
            y = True
        try:
            if float(column[13]):
                pass
        except:
            return HttpResponse("enter float ")
        counter += 1

        myibj = clonePOJ.objects.create(date=temp_date,
                                        company_name_id=f.company_name.id,
                                        location_id=f.location.id,
                                        jewellery_id=f.jewellery.id,
                                        center_stone_id=f.center_stone.id,
                                        color_of_center_stone_id=f.color_of_center_stone.id,
                                        shape_id=f.shape.id,
                                        metal_id=f.metal.id,
                                        center_stone_pieces=column[9],
                                        center_stone_weight=column[10],
                                        grosswt=column[11],
                                        cert_id=f.cert.id,
                                        pcs=column[13],
                                        amount=float(column[14]),
                                        discount_amount=float(column[16]),
                                        discount=float(column[15]),
                                        total=float(column[17]),
                                        purchase_approval=y,
                                        currency_id=f.currency.id,
                                        tag_price=float(column[19]),
                                        rate=float(column[20]),
                                        comment=column[22],
                                        )
    messages.success(request, "Successfully uploaded records")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def itemsearch(request):
    if request.method == "POST":
        query_name = request.POST.get('Stockid', None)
        if query_name:
            h = re.findall("[0-9]+", query_name)
            if len(h) == 0:
                return render(request, 'itemsearch.html', {"message": "No Records Found"})

            elif query_name.startswith("C") or query_name.startswith("c"):
                id = int(h[0])
                purchasecsobj = PurchaseOfColorStones.objects.filter(id=id)
                salescsobj = Salesofcolorstones.objects.filter(
                    stockid=str("C-")+str(id))
                if(len(purchasecsobj) == 0 and len(salescsobj) == 0):
                    context = {
                        "purcsobj": purchasecsobj,
                        "salescsobj": salescsobj,
                        "message": "No Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                elif (len(purchasecsobj) == 0 and len(salescsobj) > 0):
                    context = {
                        "purcsobj": purchasecsobj,
                        "salescsobj": salescsobj,
                        "message": "No Purchase Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)

                elif(len(purchasecsobj) > 0 and len(salescsobj) == 0):
                    context = {
                        "purcsobj": purchasecsobj,
                        "salescsobj": salescsobj,
                        "message": "No Sales Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                else:
                    context = {
                        "purcsobj": purchasecsobj,
                        "salescsobj": salescsobj,

                    }
                    return render(request, "itemsearch.html", context=context)
            elif query_name.startswith("J") or query_name.startswith("j"):
                id = int(h[0])
                purchasejobj = POJ.objects.filter(id=id)
                salesjobj = Salesofjewellery.objects.filter(
                    stockid=str("J-")+str(id))
                if(len(purchasejobj) == 0 and len(salesjobj) == 0):
                    context = {
                        "purjobj": purchasejobj,
                        "salesjobj": salesjobj,
                        "message": "No Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                elif (len(purchasejobj) == 0 and len(salesjobj) > 0):
                    context = {
                        "purjobj": purchasejobj,
                        "salesjobj": salesjobj,
                        "message": "No Purchase Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)

                elif(len(purchasejobj) > 0 and len(salesjobj) == 0):
                    context = {
                        "purjobj": purchasejobj,
                        "salesjobj": salesjobj,
                        "message": "No Sales Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                else:
                    context = {
                        "purjobj": purchasejobj,
                        "salesjobj": salesjobj,

                    }
                    return render(request, "itemsearch.html", context=context)
            elif query_name.startswith("D") or query_name.startswith("d"):
                id = int(h[0])
                purchasedobj = POD.objects.filter(id=id)
                salesdobj = Salesofdiamond.objects.filter(
                    stockid=str("D-")+str(id))
                if(len(purchasedobj) == 0 and len(salesdobj) == 0):
                    context = {
                        "purdobj": purchasedobj,
                        "salesdobj": salesdobj,
                        "message": "No Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                elif (len(purchasedobj) == 0 and len(salesdobj) > 0):
                    context = {
                        "purdobj": purchasedobj,
                        "salesdobj": salesdobj,
                        "message": "No Purchase Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)

                elif(len(purchasedobj) > 0 and len(salesdobj) == 0):
                    context = {
                        "purdobj": purchasedobj,
                        "salesdobj": salesdobj,
                        "message": "No Sales Records Found",

                    }
                    return render(request, "itemsearch.html", context=context)
                else:
                    context = {
                        "purdobj": purchasedobj,
                        "salesdobj": salesdobj,

                    }
                    return render(request, "itemsearch.html", context=context)
            else:
                return render(request, 'itemsearch.html', {"message": "No Records Found"})

    return render(request, "itemsearch.html")

    # h=re.findall("[0-9]+",query_name)
    # query_name.startswith("J")
    # isj= int(h[0])

    # results =  POJ.objects.filter(id=isj)
    # salesres = Salesofjewellery.objects.filter(stockid=query_name)
    # if len(salesres)!=0 or len(results)!=0:

    #          context = {
    #             "results":results,
    #             "salesres":salesres,
    #              }
    #          return render(request, 'itemsearchj.html', context=context)
    # else:
    #


@login_required
def colorstone_upload(request):
    template = "colorstoneupload.html"
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    column_names = str(next(io_string))
    counter = 1
    column_names = column_names.split(",")
    for column in csv.reader(io_string, delimiter=','):
        # datere=re.findall(r'\d{2}/\d{2}/\d{4}',column[0])
        # date_value=list(datere[0])
        # final_date=datetime.date(int(''.join(date_value[6:])),int(''.join(date_value[3:4])),int(''.join(date_value[0:2])))
        temp_date = datetime.datetime.strptime(
            str(column[0]), "%d-%m-%Y").date()
        f = clonePurchaseOfColorStones
        for i in range(len(column)):
            if(i == 1 or i == 8 or i == 12 or i == 25):
                continue
            if(column[i] == ""):
                messages.error(request, "ERROR: {} cannot be empty for entry:  {}. Please remove all the entries from 1 to {} in the CSV file and try again.".format(
                    column_names[i], str(counter), str(counter-1)))
                return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.company_name = companyinfo.objects.get(
                company_name=column[2].lower())
        except ObjectDoesNotExist:
            messages.error(
                request, "Company Name -> {} does not exist, Add company from top bar!\n Also remove all the enteries prior to {}".format(column[2], str(counter - 1)))
            return redirect(request.META.get('HTTP_REFERER'))
        try:
            if(column[3] == ""):
                messages.error(
                    request, "ERROR: Location cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.location, lcobj = location.objects.get_or_create(
                place=column[3].lower())
            if lcobj:
                f.location.save()
        except Exception as e:
            raise e
        try:
            if(column[4] == ""):
                messages.error(
                    request, "ERROR: Shape cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.shape, sobj = shape_cs.objects.get_or_create(
                shape=column[4].lower())
            if sobj:
                f.shape.save()
        except Exception as e:
            raise e
        try:
            if(column[5] == ""):
                messages.error(
                    request, "ERROR: GEM Type cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.gem_type, jlobj = gemtype.objects.get_or_create(
                gem=column[5].lower())
            if jlobj:
                f.gem_type.save()
        except Exception as e:
            raise e
        try:
            if(column[10] == ""):
                messages.error(
                    request, "ERROR: Colour cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.colour, colourobj = color_of_colorstone.objects.get_or_create(
                color=column[10].lower())
            if colourobj:
                f.colour.save()

        except Exception as e:
            raise e

        try:
            if(column[6] == ""):
                messages.error(
                    request, "ERROR: Origin cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.origin, clobj = Origin_cs.objects.get_or_create(
                org=column[6].lower())
            if clobj:
                f.origin.save()
        except Exception as e:
            raise e
        try:
            if(column[7] == ""):
                messages.error(
                    request, "ERROR: Treatment cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.Treatment, clsobj = Treatment_cs.objects.get_or_create(
                treatment=column[7].lower())
            if clsobj:
                f.Treatment.save()
        except Exception as e:
            raise e
        # f.Treatment=Treatment_cs.objects.get(Treatment=column[7])

        # try:
        #     f.certificate_no,cerobj = cert_no_cs.objects.get_or_create(cert=column[9].lower())
        #     if cerobj :
        #         f.certificate_no.save()
        # except Exception as e:
        #     raise e

        try:
            f.lab, mobj = Lab_cs.objects.get_or_create(lab=column[12].lower())
            if mobj:
                f.lab.save()
        except Exception as e:
            raise e

        try:
            if(column[22] == ""):
                messages.error(
                    request, "ERROR: Currency cannot be empty.For entry number: " + str(counter))
                return redirect(request.META.get('HTTP_REFERER'))
            f.currency, crobj = currencies.objects.get_or_create(
                currency=column[22].lower())
            if crobj:
                f.currency.save()
        except Exception as e:
            raise e

        if(column[21].lower() == "no"):
            y = False
        else:
            y = True
        try:
            f.tag_price = float(column[23])
        except:
            messages.error(request, "Tag Price cannot be empty. Provide 0")
            return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.rate = float(column[24])
        except:
            messages.error(request, "Rate cannot be empty. Provide 0")
            return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.Clarity = (column[8])
        except:
            messages.error(request, "Rate cannot be empty. Provide any value")
            return redirect(request.META.get('HTTP_REFERER'))

        counter += 1
        myibj = clonePurchaseOfColorStones.objects.create(date=temp_date,
                                                          company_name_id=f.company_name.id,
                                                          location_id=f.location.id,
                                                          shape_id=f.shape.id,
                                                          gem_type_id=f.gem_type.id,
                                                          origin_id=f.origin.id,
                                                          Treatment_id=f.Treatment.id,
                                                          Clarity=f.Clarity,
                                                          certificate_no=column[9].lower(
                                                          ),
                                                          colour_id=f.colour.id,
                                                          measurements=column[11],
                                                          lab_id=f.lab.id,
                                                          PCS=column[13],
                                                          Weight=column[14],
                                                          Price=column[15],
                                                          units=column[16],
                                                          amount=float(
                                                              column[17]),
                                                          discount_amount=float(
                                                              column[19]),
                                                          discount=float(
                                                              column[18]),
                                                          total_val=float(
                                                              column[20]),
                                                          purchaseapv=y,
                                                          currency_id=f.currency.id,
                                                          tag_price=f.tag_price,
                                                          rate=f.rate,
                                                          comment=column[25]
                                                          )
    messages.success(request, "Successfully uploaded records")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def diamond_upload(request):
    template = "diamondupload.html"
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    column_names = str(next(io_string))
    counter = 1
    column_names = column_names.split(",")
    for column in csv.reader(io_string, delimiter=','):
        temp_date = datetime.datetime.strptime(
            str(column[0]), "%d-%m-%Y").date()

        f = clonePOD
        for i in range(len(column)):
            if(i == 1 or i == 8 or i == 12):
                continue
            if(column[i] == ""):
                messages.error(request, "ERROR: {} cannot be empty for entry:  {}. Please remove all the entries from 1 to {} in the CSV file and try again.".format(
                    column_names[i], str(counter), str(counter-1)))
                return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.company_name = companyinfo.objects.get(
                company_name=column[2].lower())
        except ObjectDoesNotExist:
            messages.error(
                request, "Company Name -> {} does not exist, Add company from top bar!\n Also remove all the enteries prior to {}".format(column[2], str(counter - 1)))
            return redirect(request.META.get('HTTP_REFERER'))
        try:
            f.location, lcobj = location.objects.get_or_create(
                place=column[3].lower())
            if lcobj:
                f.location.save()
        except Exception as e:
            raise e
        try:
            f.shape, slobj = shape_d.objects.get_or_create(
                shape=column[4].lower())
            if slobj:
                f.shape.save()
        except Exception as e:
            raise e
        try:
            f.clarity, clobj = clarity.objects.get_or_create(
                clarity=column[5].lower())
            if clobj:
                f.clarity.save()
        except Exception as e:
            raise e
        try:
            f.color_origin1, colobj = color_origin.objects.get_or_create(
                c_o=column[6].lower())
            if colobj:
                f.color_origin1.save()
        except Exception as e:
            raise e
        try:
            f.white_color_grade1, fgobj = white_color_grade.objects.get_or_create(
                w_c_g=column[7].lower())
            if fgobj:
                f.white_color_grade1.save()
        except Exception as e:
            raise e

        try:
            f.cut, cobj = cut.objects.get_or_create(cut=column[9].lower())
            if cobj:
                f.cut.save()
        except Exception as e:
            raise e

        try:
            f.polish, plobj = polish.objects.get_or_create(
                polish=column[10].lower())
            if plobj:
                f.polish.save()
        except Exception as e:
            raise e
        try:
            f.symmetry, syobj = symmetry.objects.get_or_create(
                symmetry=column[11].lower())
            if syobj:
                f.symmetry.save()
        except Exception as e:
            raise e
        try:
            f.fluorescence_intensity, fiobj = fluorescence_intensity.objects.get_or_create(
                f_intensity=column[15].lower())
            if fiobj:
                f.fluorescence_intensity.save()
        except Exception as e:
            raise e
        try:
            f.fluorescence_color, fcobj = fluorescence_color.objects.get_or_create(
                f_color=column[16].lower())
            if fcobj:
                f.fluorescence_color.save()
        except Exception as e:
            raise e
        try:
            f.certificate_d, ceobj = certificate_d.objects.get_or_create(
                certd=column[18].lower())
            if ceobj:
                f.certificate_d.save()
        except Exception as e:
            raise e
        try:
            f.currency, crobj = currencies.objects.get_or_create(
                currency=column[28].lower())
            if crobj:
                f.currency.save()
        except Exception as e:
            raise e
        if column[19].lower() == "yes":
            bools1 = True
        else:
            bools1 = False
        if column[31].lower() == "yes":
            bools = True
        else:
            bools = False
        counter += 1
        myibj = clonePOD.objects.create(date=temp_date,
                                        company_name_id=f.company_name.id,
                                        location_id=f.location.id,
                                        shape_id=f.shape.id,
                                        clarity_id=f.clarity.id,
                                        color_origin1_id=f.color_origin1.id,
                                        white_color_grade1_id=f.white_color_grade1.id,
                                        fancycolor_grade=column[8],
                                        cut_id=f.cut.id,
                                        polish_id=f.polish.id,
                                        symmetry_id=f.symmetry.id,
                                        measurements=column[12],
                                        depth=column[13],
                                        table_perc=column[14],
                                        fluorescence_intensity_id=f.fluorescence_intensity.id,
                                        fluorescence_color_id=f.fluorescence_color.id,
                                        certificate_no_d=column[17],
                                        certificate_d_id=f.certificate_d.id,
                                        laser_inscription=bools1,
                                        PCS_d=column[20],
                                        weight_d=float(column[21]),
                                        price=float(column[22]),
                                        units=column[23],
                                        amount_d=float(column[24]),
                                        DIS_Amount_d=float(column[26]),
                                        DIS_d=float(column[25]),
                                        total_val_d=float(column[27]),
                                        currency_id=f.currency.id,
                                        tag_price_d=float(column[29]),
                                        rate_d=float(column[30]),
                                        purchaseapv_d=bools,
                                        comment=column[32],
                                        )
    messages.success(request, "Successfully uploaded records")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def show_on_frontend_d(request, id):
    obj = Inventoryofdiamond.objects.get(id=id)
    obj.frontend = True
    obj.save()
    return redirect('delete-d')


@login_required
def hide_from_frontend_d(request, id):
    obj = Inventoryofdiamond.objects.get(id=id)
    obj.frontend = False
    obj.save()
    return redirect('delete-d')


@login_required
def show_on_frontend_cs(request, id):
    obj = Inventoryofcolorstones.objects.get(id=id)
    obj.frontend = True
    obj.save()
    return redirect('delete-cs')


@login_required
def hide_from_frontend_cs(request, id):
    obj = Inventoryofcolorstones.objects.get(id=id)
    obj.frontend = False
    obj.save()
    return redirect('delete-cs')


@login_required
def show_on_frontend_jewel(request, id):
    obj = Inventoryofjewellery.objects.get(id=id)
    obj.frontend = True
    obj.save()
    return redirect('delete-jewell')


@login_required
def hide_from_frontend_jewel(request, id):
    obj = Inventoryofjewellery.objects.get(id=id)
    obj.frontend = False
    obj.save()
    return redirect('delete-jewell')


@login_required
def get_company_details(request):
    if request.is_ajax:
        name = request.GET.get('name', 'None')
        name = name.lower()
        if companyinfo.objects.filter(company_name=name).exists():
            company = companyinfo.objects.get(company_name=name)
            return JsonResponse({"contact_no": company.contact, "location": company.address}, status=200)
    return JsonResponse({}, status=200)


@login_required
def jewel_metal_filter(request, value, category):
    if category == "color_of_center_stone":
        jw = Inventoryofjewellery.objects.filter(
            Q(color_of_center_stone=value) & Q(frontend=True))
        if len(jw) == 0:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "metalcat": jw,
            }

        return render(request, "filtered.html", context=context)
    elif category == "jewellery_type":
        jw = Inventoryofjewellery.objects.filter(
            Q(jewellery_type=value) & Q(frontend=True))
        if jw is None:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "metalcat": jw,
            }
        return render(request, "filtered.html", context=context)
    elif category == "center_stone":
        jw = Inventoryofjewellery.objects.filter(
            Q(center_stone=value) & Q(frontend=True))
        if jw is None:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "metalcat": jw,
            }
        return render(request, "filtered.html", context=context)
    else:
        pass


@login_required
def jewel_listing(request):
    return render(request, "jewel_listing.html")


@login_required
def contactsendmail(request):
    if request.method == "GET":
        form = contactformemail()
    else:
        form = contactformemail(request.POST)
        if form.is_valid():
            fromemail = form.cleaned_data["fromemail"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_mail(subject, message, fromemail, [
                      'krgconnect86@gmail.com', fromemail])
    return render(request, 'contact.html', {'form': form})


@login_required
def diamond_filter(request, value, category):
    if category == "polish":
        dm = Inventoryofdiamond.objects.filter(Q(polish=value))
        if dm is None:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "diamcat": dm,
            }
        return render(request, "filtered_d.html", context=context)
    elif category == "white_color_grade1":
        dm = Inventoryofdiamond.objects.filter(Q(white_color_grade1=value))
        if dm is None:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            # 'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "diamcat": dm,
            }

        return render(request, "filtered_d.html", context=context)
    else:
        pass


@login_required
def diamond_listing(request):
    return render(request, "diamond_listing.html")


@login_required
def cs_filter(request, value, category):
    if category == "origin":
        clst = Inventoryofcolorstones.objects.filter(Q(origin=value))
        if len(clst) == 0:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "cscat": clst,
            }

        return render(request, "filtered_cs.html", context=context)
    elif category == "treatment":
        clst = Inventoryofcolorstones.objects.filter(Q(treatment=value))
        if len(clst) == 0:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "cscat": clst,
            }
        return render(request, "filtered_cs.html", context=context)
    elif category == "shape":
        clst = Inventoryofcolorstones.objects.filter(Q(shape=value))
        if len(clst) == 0:
            message = "No records found"
            context = {
                'message': message,
            }
        else:
            jewel_colors = colorofcstone.objects.all()
            jewel_types = set(Inventoryofjewellery.objects.values_list(
                'jewellery_type', flat=True))
            center_stone_types = set(
                Inventoryofjewellery.objects.values_list('center_stone', flat=True))
            # diam_fci = set(Inventoryofdiamond.objects.values_list(
            #     'fancy_color_intensity1', flat=True))
            diam_pol = set(
                Inventoryofdiamond.objects.values_list('polish', flat=True))
            diam_wcg1 = set(Inventoryofdiamond.objects.values_list(
                'white_color_grade1', flat=True))
            cs_treatment = set(
                Inventoryofcolorstones.objects.values_list('treatment', flat=True))
            cs_origin = set(
                Inventoryofcolorstones.objects.values_list('origin', flat=True))
            cs_shape = set(
                Inventoryofcolorstones.objects.values_list('shape', flat=True))

            context = {
                'gemstones': jewel_colors,
                'jewel_types': jewel_types,
                'center_stone_types': center_stone_types,
                # 'diam_fancy_color_intensity1': diam_fci,
                'diam_polish': diam_pol,
                'diamwcg': diam_wcg1,
                'cs_tr': cs_treatment,
                'cs_org': cs_origin,
                'cs_shpe': cs_shape,
                "cscat": clst,
            }

        return render(request, "filtered_cs.html", context=context)
    else:
        pass


@login_required
def cstone_listing(request):
    return render(request, "cstone_listing.html")


@login_required
def ExportPurchaseOfColorStones(request):
    objects = PurchaseOfColorStones.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "PurchaseRecordsofColourStones " + \
        str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'SHAPE', 'GEM TYPE',
                     'ORIGIN', 'TREATMENT', 'CLARITY', 'CERTIFICATE NUMBER',
                    'LAB', 'COLOUR', 'MEASUREMENTS', 'PCS', 'WEIGHT', 'PRICE/CT', 'UNITS', 'AMOUNT', 'DISCOUNT %', 'DICOUNT AMOUNT',  'TOTAL AMOUNT', 'BOUGHT', 'CURRENCY', 'TAG PRICE', 'RATE', 'COMMENTS'])
    for item in objects:
        if item.purchaseapv:
            z = "Yes"
        else:
            z = "No"
        output.append([item.date, 'C-' + str(item.id), item.company_name, item.location, item.shape.shape, item.gem_type.gem, item.origin.org, item.Treatment.treatment, item.Clarity, item.certificate_no, item.lab, item.colour,
                      item.measurements,  item.PCS, item.Weight, item.Price, item.units, item.amount, item.discount, item.discount_amount, item.total_val, z, item.currency, item.tag_price, item.rate, item.comment])

    writer.writerows(output)
    return response


@login_required
def ExportInventoryofcolorstones(request):
    objects = Inventoryofcolorstones.objects.filter(appvreturnstatus=False)
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "InventoryofColourStones "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['STOCK ID', 'LOCATION', 'SHAPE', 'GEM TYPE', 'ORIGIN', 'TREATMENT',
                    'CLARITY', 'CERTIFICATE NUMBER', 'LAB', 'COLOUR', 'MEASUREMENTS',  'PCS', 'WEIGHT', 'UNITS', 'TAG PRICE'])
    for item in objects:
        output.append([item.stockid, item.location, item.shape, item.gem_type, item.origin, item.treatment, item.Clarity,
                      item.certificate_no, item.lab, item.color, item.measurements,  item.PCS, item.Weight, item.units, item.tag_price])

    writer.writerows(output)
    return response


@login_required
def ExportSalesofcolorstones(request):
    objects = Salesofcolorstones.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "SalesofColourStones "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'SHAPE', 'GEM TYPE', 'ORIGIN', 'TREATMENT', 'CLARITY', 'CERTIFICATE',  'LAB',
                    'COLOUR', 'MEASUREMENTS', 'PCS', 'WEIGHT', 'PRICE/CT', 'AMOUNT', 'DISCOUNT %', 'DICOUNT AMOUNT', 'TOTAL AMOUNT', 'CURRENCY', 'TAG PRICE', 'RATE', 'SOLD', 'COMMENTS'])
    for item in objects:
        if item.salesapprovalstatus_cs is True:
            z = "Yes"
        else:
            z = "No"
        output.append([item.date, item.stockid, item.company_name, item.location, item.shape, item.gem_type, item.origin, item.treatment, item.Clarity, item.certificate_no, item.lab, item.color,
                      item.measurements,  item.PCS, item.Weight_cs, item.price, item.amount_cs, item.DIS_cs, item.DIS_amount_cs, item.total_value_cs, item.currency_cs, item.tag_price_cs, item.rate_cs, z, item.comment])

    writer.writerows(output)
    return response


@login_required
def get_certificate_of_colorstone(request):
    stockid = request.GET.get('stockid', None)
    try:
        id_used = Inventoryofcolorstones.objects.get(stockid=stockid)
        data = ColorStone_media.objects.get(stockid=id_used.id)
        return JsonResponse({'certificate': str(data.certificate)}, status=200)
    except:
        data = {}
    return JsonResponse({'certificate': '0'}, status=200)


@login_required
def ExportSalesReturnCS(request):
    objects = Salesreturn_cs.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "Salesreturncolorstones "+str(datetime.datetime.now())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME',
                    'LOCATION', 'GEM TYPE', 'COLOUR', 'WEIGHT ', 'PRICE/CT', 'TOTAL AMOUNT', 'CURRENCY'])
    for item in objects:
        output.append([item.date, item.stockid, item.company_name,
                      item.location, item.gem_type, item.colour, item.weight, item.price, item.total_amount, item.currency])
    writer.writerows(output)
    return response


@login_required
def ExportPOJ(request):
    objects = POJ.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "PurchaseRecordsofJewellery "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'JEWELLERY TYPE', 'CENTER STONE', 'COLOR OF CENTER STONE', 'SHAPE', 'METAL', 'CENTER STONE PIECES',
                    'CENTER STONE WEIGHT', 'GROSS WEIGHT', 'CERTIFICATE TYPE', 'PCS',  'AMOUNT', 'DISCOUNT %', 'DISCOUNT AMOUNT', 'TOTAL AMOUNT', 'BOUGHT', 'CURRENCY', 'TAG PRICE', 'RATE', 'COMMENTS'])
    for item in objects:
        if item.purchase_approval:
            z = "Yes"
        else:
            z = "No"
        output.append([item.date, 'J-' + str(item.id), item.company_name, item.location.place.title(), item.jewellery.jewel.title(), item.center_stone.stone.title(), item.color_of_center_stone.color.title(), item.shape.shape.title(), item.metal.metal.title(),
                      item.center_stone_pieces, item.center_stone_weight, item.grosswt, item.cert.cert.upper(), item.pcs, item.amount, item.discount, item.discount_amount, item.total, z, item.currency.currency.upper(), item.tag_price, item.rate, item.comment])

    writer.writerows(output)
    return response


@login_required
def ExportInventoryofjewellery(request):
    objects = Inventoryofjewellery.objects.filter(appvreturnstatus=False)
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "InventoryofJewellery "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['STOCK ID', 'LOCATION', 'JEWELLERY TYPE', 'CENTER STONE', 'COLOR OF CENTER STONE', 'SHAPE',
                    'METAL', 'CENTER STONE PIECES', 'CENTER STONE WEIGHT', 'GROSS WEIGHT', 'LAB', 'PCS',  'TAG PRICE'])
    for item in objects:
        output.append([item.stockid, item.location.place.title(), item.jewellery_type.jewel.title(), item.center_stone.stone.title(), item.color_of_center_stone.color.title(
        ), item.shape.shape.title(), item.metal.metal.title(), item.center_stone_pieces, item.center_stone_weight, item.grosswt, item.cert.cert.upper(), item.pcs, item.tag_price])

    writer.writerows(output)
    return response


@login_required
def ExportSalesofjewellery(request):
    objects = Salesofjewellery.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "SalesofJewellery "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])

    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'JEWELLERY TYPE', 'CENTER STONE', 'COLOUR OF CENTER STONE', 'SHAPE', 'METAL', 'CENTER STONE PIECES',
                    'CENTER STONE WEIGHT', 'GROSS WEIGHT', 'CERTIFICATE TYPE', 'PCS',  'AMOUNT', 'DISCOUNT %', 'DISCOUNT AMOUNT', 'TOTAL AMOUNT', 'CURRENCY', 'TAG PRICE', 'RATE', 'SOLD ITEM', 'COMMENTS'])
    for item in objects:
        if item.salesapprovalstatus:
            z = "Yes"
        else:
            z = "No"
        output.append([item.date, item.stockid, item.company_name, item.location.place.title(), item.jewellery_type.jewel.title(), item.center_stone.stone.title(), item.color_of_center_stone.color.title(), item.shape.shape.title(), item.metal.metal.title(
        ), item.center_stone_pieces, item.center_stone_weight, item.gross_wt, item.certificate.cert.upper(), item.PCS, item.amount, item.DIS, item.DIS_amount, item.total_value, item.currency.currency.upper(), item.tag_price, item.rate, z, item.comment])

    writer.writerows(output)
    return response


@login_required
def ExportSalesReturn(request):
    objects = Salesreturn.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "SalesreturnJewellery "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['RETURNED DATE', 'STOCK ID', 'COMPANY NAME',
                    'LOCATION', 'JEWELLERY TYPE', 'GROSS WEIGHT', 'TOTAL AMOUNT', 'CURRENCY'])
    for item in objects:
        output.append([item.date, item.stockid, item.company_name, item.location.title(
        ), item.jewellery_type.title(), item.grosswt, item.total_amount, item.currency])

    writer.writerows(output)
    return response


@login_required
def ExportPOD(request):
    objects = POD.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "PurchaseOfDiamonds "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'SHAPE', 'CLARITY', 'COLOR ORIGIN', 'WHITE COLOR GRADE', 'FANCY COLOR GRADE ', 'CUT', 'POLISH', 'SYMMETRY', 'MEASUREMENTS', 'DEPTH %', 'TABLE %', 'FLUORESCENCE INTENSITY',
                    'FLUORESCENCE COLOR', 'CERTIFICATE NUMBER', 'CERTIFICATE TYPE', 'LASER INSCRIPTION', 'PCS', 'WEIGHT', 'PRICE', 'UNITS', 'AMOUNT', 'DISCOUNT %', 'DISCOUNT AMOUNT', 'TOTAL AMOUNT', 'CURRENCY', 'TAG PRICE', 'RATE', 'BOUGHT', 'COMMENTS'])
    for item in objects:

        if item.laser_inscription is True:
            bools = "Yes"
        else:
            bools = "No"
        if item.purchaseapv_d is False:
            bools1 = "No"
        else:
            bools1 = "Yes"
        output.append([item.date, 'D-' + str(item.id), item.company_name.company_name.title(), item.location.place.title(), item.shape.shape.title(), item.clarity.clarity.title(), item.color_origin1.c_o.title(), item.white_color_grade1.w_c_g.title(), item.fancycolor_grade.title(), item.cut.cut.title(), item.polish.polish.title(), item.symmetry.symmetry.title(), item.measurements,
                      item.depth, item.table_perc, item.fluorescence_intensity.f_intensity.title(), item.fluorescence_color.f_color.title(), item.certificate_no_d, item.certificate_d.certd.upper(), bools, item.PCS_d, item.weight_d, item.price, item.units, item.amount_d, (item.DIS_d), item.DIS_Amount_d, item.total_val_d, item.currency.currency.upper(), item.tag_price_d, item.rate_d, bools1, item.comment])

    writer.writerows(output)

    return response


@login_required
def ExportInventoryofdiamond(request):
    objects = Inventoryofdiamond.objects.filter(appvreturnstatus_d=False)
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "InventoryofDiamonds "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['STOCK ID', 'LOCATION', 'SHAPE', 'CLARITY', 'COLOUR ORIGIN', 'WHITE COLOUR GRADE', 'FANCY COLOUR GRADE', 'CUT', 'POLISH', 'SYMMETRY', 'MEASUREMENTS',
                    'DEPTH %',  'TABLE %', 'FLUORESCENCE INTENSITY', 'FLUORESECENE COLOUR', 'CERTIFICATE NUMBER', ' LAB', 'LASER INSCRIPTION', 'PCS', 'WEIGHT', 'UNITS', 'TAG PRICE'])
    for item in objects:
        if item.laser_inscription is True:
            bools = "Yes"
        else:
            bools = "No"

        output.append([item.stockid, item.location.place.title(), item.shape.shape.title(), item.clarity.clarity.title(), item.color_origin1.c_o, item.white_color_grade1, item.fancycolor_grade, item.cut, item.polish, item.symmetry,
                      item.measurements, item.depth, item.table, item.fluorescence_intensity, item.fluorescence_color, item.certificate_no_d, item.certificate_d, bools, item.PCS_d, item.weight_d, item.units, item.tag_price_d])

    writer.writerows(output)
    return response


@login_required
def ExportSalesofdiamond(request):
    objects = Salesofdiamond.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "SalesofDiamonds "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION', 'SHAPE', 'CLARITY', 'COLOR ORIGIN', 'WHITE COLOUR GRADE', 'FANCY COLOUR GRADE ', 'CUT', 'POLISH', 'SYMMETRY', 'MEASUREMENTS',  'DEPTH %', 'TABLE %',
                    'FLUORESCENCE INTENSITY', 'FLUORESCENCE COLOR', 'CERTIFICATE NUMBER', 'LAB', 'LASER INSCRIPTION', 'PCS', 'WEIGHT', 'PRICE/CT', 'UNITS', 'AMOUNT', 'DISCOUNT %', 'DISCOUNT AMOUNT', 'TOTAL AMOUNT', 'CURRENCY', 'TAG PRICE', 'RATE', 'SOLD', 'COMMENTS'])
    for item in objects:
        if item.laser_inscription is True:
            bools = "Yes"
        else:
            bools = "No"
        if item.salesapprovalstatus_d is True:
            bools1 = "Yes"
        else:
            bools1 = "No"

        output.append([item.date, item.stockid, item.company_name, item.location, item.shape, item.clarity, item.color_origin1, item.white_color_grade1, item.fancycolor_grade, item.cut, item.polish, item.symmetry, item.measurements, item.depth, item.table, item.fluorescence_intensity,
                      item.fluorescence_color, item.certificate_no_d, item.certificate_d, bools, item.PCS_d, item.weight_d, item.price, item.units, item.amount_d, item.DIS_d, item.DIS_Amount_d, item.total_value_d, item.currency, item.tag_price_d, item.rate_d, bools1, item.comment])

    writer.writerows(output)
    return response


@login_required
def get_certificate_of_jewellery(request):
    stockid = request.GET.get('stockid', None)
    try:
        value = Inventoryofjewellery.objects.get(stockid=stockid)
        data = Jewel_media.objects.get(jewel_object=value.id)

        return JsonResponse({'certificate': str(data.certificate)}, status=200)
    except:
        data = {}
    return JsonResponse({'certificate': '0'}, status=200)


@login_required
def get_certificate_of_diamond(request):
    stockid = request.GET.get('stockid', None)
    try:
        value = Inventoryofdiamond.objects.get(stockid=stockid)
        data = Diamond_media.objects.get(Diamond_object=value.id)

        return JsonResponse({'certificate': str(data.certificate)}, status=200)
    except:
        data = {}
    return JsonResponse({'certificate': '0'}, status=200)


@login_required
def ExportSalesReturnDiamonds(request):
    objects = Salesreturn_d.objects.all()
    output = []
    response = HttpResponse(content_type='text/csv')
    filename = "Salesreturndiamonds "+str(datetime.date.today())+".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(
        filename)
    writer = csv.writer(response)
    writer.writerow(['SDS GEMS'])
    writer.writerow(['EC-2050, BHARAT DIAMOND BOURSE, BKC, MUMBAI-400051'])
    writer.writerow(['RETURNED DATE', 'STOCK ID', 'COMPANY NAME', 'LOCATION',
                    'SHAPE', 'WEIGHT', 'COLOUR', 'CLARITY', 'PRICE/CT', 'TOTAL AMOUNT', 'CURRENCY'])
    for item in objects:
        output.append([item.date, item.stockid, item.company_name, item.location,
                      item.shape, item.weight, item.colour, item.clarity, item.price, item.totalamount, item.currency])

    writer.writerows(output)
    return response
