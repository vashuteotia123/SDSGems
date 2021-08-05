from django.http.response import HttpResponse
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
    # countone=POJ.objects.all().count()
    # print(countone)
    if(form.is_valid()):
        # jeweltype = form.cleaned_data["jeweltype"]
        # invt_data = invrt.objects.all()
        # if jeweltype in invt_data.jeweltype:
        #     get_object = invt.objects.get(jeweltype=jeweltype))
        #     curr_pieces = form.cleaned_data['pieces']
        #     get_object.pieces += curr_pieces
        # else:
        #     new_object = invrt(jeweltype=form.cleaned_data['jeweltpye'], pieces=form.cleaned_data['pieces'])
        
        #call inventory save method here for stockid?
        # Inventoryofjewellery.obj.save()
        form.save()
       
            
        return render(request,"index.html")
    context={
        "formshow":form,
    }
    return render(request,"form.html",context=context)

def formsubmit(request):
    return render(request,"index.html")

# def showform1(request):
#     form=POCSForm(request.POST)
#     if(form.is_valid()):
        # jeweltype = form.cleaned_data["jeweltype"]
        # invt_data = invrt.objects.all()
        # if jeweltype in invt_data.jeweltype:
        #     get_object = invt.objects.get(jeweltype=jeweltype))
        #     curr_pieces = form.cleaned_data['pieces']
        #     get_object.pieces += curr_pieces
        # else:
        #     new_object = invrt(jeweltype=form.cleaned_data['jeweltpye'], pieces=form.cleaned_data['pieces'])
    #     obj1=Inventoryofcolorstones.objects.create(location=form.cleaned_data['location'],shape=form.cleaned_data['shape'],gem_type=form.cleaned_data['gem_type']
    #     ,weight=form.cleaned_data['weight'],origin=form.cleaned_data['origin'],treatment=form.cleaned_data['treatment']
    #     ,certificate_no_cs=form.cleaned_data['certificate_no_cs'],color=form.cleaned_data['color'],measurements=form.cleaned_data['measurements']
    #     ,lab=form.cleaned_data['lab'],tag_price_cs=form.cleaned_data['tag_price_cs'])
        
    #     form.save()  #data extract
    #     return render(request,"index.html")
    # context={
    #     "formshow":form,
    # }
    # return render(request,"form.html",context=context)


def showform2(request):
    form2=PODForm(request.POST)
    if(form2.is_valid()):

        form2.save()
        return render(request,"index.html")
    context={
        "formshow2":form2,
    }
    return render(request,"form2.html",context=context)

    
    



    




# def load_currency(request):
#     country_id = request.POST.get("country_id")
#     currency = currencies.objects.filter(country_id=country_id).all()
#     return render(request, 'templates/currency_dropdown_list_options.html', {'currency' : currency})



def deleteid(request,idno):
    current=Inventoryofjewellery.objects.get(id=idno)
    current.delete()
    return render(request,"delete.html")

def showjewell(request):
    objjewell=Inventoryofjewellery.objects.all()
    context={
        "showjewellery":objjewell,
    }
    return render(request,"showj.html",context=context)
    
# def delete(request, idno):
#     query = Inventoryofjewellery.objects.get(pk=idno)
#     query.delete()
#     return HttpResponse("Deleted!")