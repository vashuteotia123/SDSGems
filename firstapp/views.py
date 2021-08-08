from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

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
    form = POJForm(request.POST)
    # countone=POJ.objects.all().count()
    # print(countone)
    if(form.is_valid()):
        form.save()

        return render(request, "index.html")
    context = {
        "formshow": form,
    }
    return render(request, "form.html", context=context)


def formsubmit(request):
    return render(request, "index.html")

def showform1(request):
    form1=POCSForm(request.POST)
    if(form1.is_valid()):
        #   new_object = invrt(jeweltype=form.cleaned_data['jeweltpye'], pieces=form.cleaned_data['pieces'])
    #     obj1=Inventoryofcolorstones.objects.create(location=form.cleaned_data['location'],shape=form.cleaned_data['shape'],gem_type=form.cleaned_data['gem_type']
    #     ,weight=form.cleaned_data['weight'],origin=form.cleaned_data['origin'],treatment=form.cleaned_data['treatment']
    #     ,certificate_no_cs=form.cleaned_data['certificate_no_cs'],color=form.cleaned_data['color'],measurements=form.cleaned_data['measurements']
    #     ,lab=form.cleaned_data['lab'],tag_price_cs=form.cleaned_data['tag_price_cs'])

        form1.save() 
        return render(request,"index.html")
    context={
        "formshow":form1,
    }
    return render(request,"form.html",context=context)


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

    context = {'form3':form3}
    return render(request, 'update_jewellery.html', context)

def showjewell(request):
    objjewell=POJ.objects.all()
    context={
        "showjewellery":objjewell,
    }
    return render(request,"showj.html",context=context)
    
# def delete(request, idno):
#     query = Inventoryofjewellery.objects.get(pk=idno)
#     query.delete()
#     return HttpResponse("Deleted!")

def showdiamond(request):
    diamondobj=POD.objects.all()
    context={
        "showdia":diamondobj,
    }
    return render(request,"showd.html",context=context)

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

    context = {'form4':form4}
    return render(request, 'update_diamond.html', context)

def deleteid_d(request, idno):
    current = POD.objects.get(id=idno)
    current.delete()
    return render(request, "delete.html")

def cform(request):
    comform= CompanyForm(request.POST)
    if(comform.is_valid()):

        comform.save()
        return render(request, "index.html")
    context = {
        "comform": comform,
    }
    return render(request, "cform.html",context=context)

###
#def showcs(request):
#    cs_obj=PurchaseOfColorStones.objects.all()
#    context={
#        "show_cs":cs_obj,
#    }
#   return render(request,"showcs.html",context=context)

# def update_cs(request, ck):

#     cs_obj = PurchaseOfColorStones.objects.get(id=ck)
#     form5 = POCSForm(instance=cs_obj)
#     # print("7")
#     if request.method == 'POST':
#         # print("2")
#         form5 = PODForm(request.POST, instance=cs_obj)
#         # print("3")
#         form5.save()
#         return redirect('/showcs')

#     context = {'form5':form5}
#     return render(request, 'update_cd.html', context)

# def deleteid_cs(request, idno):
#     current = PurchaseOfColorStones.objects.get(id=idno)
#     current.delete()
#     return render(request, "delete.html")

def showinvj(request):
    invjobj=Inventoryofjewellery.objects.all()
    context={
        "showinvj":invjobj,
    }
    return render(request,"showinvj.html",context=context)

def returninvj(request, id1):
    now = Inventoryofjewellery.objects.get(id=id1)
    now.delete()
    context={
        "showinvj":Inventoryofjewellery.objects.all(),
    }
    return render(request, "showinvj.html",context=context)
