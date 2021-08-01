from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'second.html')
def take_input(request):
    user_name=request.POST.get("user_name")
    email_id=request.POST.get("email_id")
    newinput=Database(username=user_name,email=email_id)
    newinput.save()
    return render(request,'second.html')
def show_data(request):
    context={
        "all_data":Database.objects.all(),
        "countone":Database.objects.all().count(),
    }
    return render(request,"show_data.html",context=context)
def showform(request):
    form=POJForm(request.POST)
    if(form.is_valid()):
        # jeweltype = form.cleaned_data["jeweltype"]
        # invt_data = invrt.objects.all()
        # if jeweltype in invt_data.jeweltype:
        #     get_object = invt.objects.get(jeweltype=jeweltype))
        #     curr_pieces = form.cleaned_data['pieces']
        #     get_object.pieces += curr_pieces
        # else:
        #     new_object = invrt(jeweltype=form.cleaned_data['jeweltpye'], pieces=form.cleaned_data['pieces'])
        obj=Inventory.objects.create(center_stone=form.cleaned_data['center_stone'],shape=form.cleaned_data['shape'])
        
        form.save()  #data extract
        return render(request,"index.html")
    context={
        "formshow":form,
    }
    return render(request,"form.html",context=context)

def formsubmit(request):
    return render(request,"index.html")


# def showform2(request):
#     form2=PODForm(request.POST)
#     if(form2.is_valid()):
        




    




# def load_currency(request):
#     country_id = request.POST.get("country_id")
#     currency = currencies.objects.filter(country_id=country_id).all()
#     return render(request, 'templates/currency_dropdown_list_options.html', {'currency' : currency})

