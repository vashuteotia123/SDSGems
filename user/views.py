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

class SignUpView(CreateView):
    template_name = 'user_register.html'
    success_url = reverse_lazy('user_login')
    form_class = UserForm


def user_login(request):
    message = None

    if 'is_logedin' not in request.session and request.method != 'POST':
        message = "Please Enter your Email  and password "
        return render(request, 'user_login.html', {'message': message})
    elif request.method == 'POST':

        user_email = request.POST.get('email')
        user_email = user_email.lower()
        user_password = request.POST.get('password')
        try:
            user_details = (User_table.objects.get(pk=user_email))
            if(user_details.password == user_password):
                if(user_details.permit_user):
                    request.session['is_logedin'] = True
                    request.session['logdin_time'] = str(datetime.datetime.now())
                    request.session['user_email'] = user_details.email_id
                    request.session['business_type'] = user_details.Businesstype
                    return redirect('/')
                else:
                    message = "You are not permitted to view the content. Contact the administrator."
            else:
                message = "Please check your credentials."
        except User_table.DoesNotExist:
            message = "No user found...!!"

        return render(request, 'user_login.html', {'message': message})

    return redirect("/")


def user_Logout(request):
    if 'is_logedin' in request.session:
        del request.session['is_logedin']
        request.session.clear()
        return redirect('user_login')
    return redirect("/")



def home(request):
    context = {}
    return render(request, 'home.html', context)

class ShopList(View):
    template_name = 'shop_list.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogList(View):
    template_name = 'blog_list.html'

    def get(self, request):
        all_blogs = Blog.objects.all()
        return render(request, self.template_name, {'all_blogs': all_blogs})

class ContactUs(View):
    template_name = 'contactus.html'

    def get(self, request):
        return render(request, self.template_name)

class MyAccount(View):
    template_name = 'myaccount.html'

    def get(self, request):
        return render(request, self.template_name)