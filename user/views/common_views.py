from django.contrib.messages.api import MessageFailure
from django.core import paginator
from django.views.generic import View
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.utils.regex_helper import Group
from django.views.generic.base import TemplateView

from firstapp.models import (
    Inventoryofcolorstones,
    Inventoryofdiamond,
    Inventoryofjewellery,
    certificate,
    color_of_colorstone,
)
from ..models import *
from ..forms import *
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
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import get_template

# Create your views here.


def myuser_login_required(f):
    def wrap(request, *args, **kwargs):
        if "is_logedin" not in request.session.keys():
            return HttpResponseRedirect("/user_login")
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


class SignUpView(CreateView):
    template_name = "user_templates/user_register.html"
    success_url = reverse_lazy("user_login")
    form_class = UserForm


def user_login(request):
    message = None

    if "is_logedin" not in request.session and request.method != "POST":
        message = "You are not logged in. Please login to continue."
        return render(request, "user_templates/user_login.html", {"message": message})
    elif request.method == "POST":

        user_email = request.POST.get("email")
        user_email = user_email.lower()
        user_password = request.POST.get("password")
        try:
            user_details = User_table.objects.get(pk=user_email)
            if user_details.password == user_password:
                if user_details.permit_user:
                    request.session["is_logedin"] = True
                    request.session["logdin_time"] = str(datetime.datetime.now())
                    request.session["user_email"] = user_details.email_id
                    request.session["business_type"] = user_details.Businesstype
                    return redirect("/")
                else:
                    message = "You are not permitted to view the content. Contact the administrator."
            else:
                message = "Please check your credentials."
        except User_table.DoesNotExist:
            message = "No user found...!!"

        return render(request, "user_templates/user_login.html", {"message": message})

    return redirect("/")


def user_Logout(request):
    if "is_logedin" in request.session:
        del request.session["is_logedin"]
        request.session.clear()
        return redirect("user_login")
    return redirect("/")


def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        Subscribed_users.objects.create(email=email)
        return render(request, "coming_soon_message.html")
    context = {}
    return render(request, "coming_soon.html", context)


class ShopList(View):
    template_name = "shop_list.html"

    def get(self, request):
        return render(request, self.template_name)


class BlogList(View):
    template_name = "blog_list.html"

    def get(self, request):
        all_blogs = Blog.objects.all()
        return render(request, self.template_name, {"all_blogs": all_blogs})


class ContactUs(View):
    template_name = "contactus.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        from_name = request.POST.get("name")
        from_mail = request.POST.get("email").lower()
        mail_subject = request.POST.get("subject")
        mail_message = request.POST.get("contactMessage")
        to_mail = "sdsgems9@gmail.com"

        ctx = {
            "from_name": from_name,
            "from_mail": from_mail,
            "mail_message": mail_message,
        }
        msg = get_template("mail.html").render(ctx)
        email = EmailMessage(mail_subject, msg, to=[to_mail])
        email.content_subtype = "html"
        email.send()
        return render(request, self.template_name)


class MyAccount(View):
    template_name = "user_templates/myaccount.html"

    def get(self, request):
        if "is_logedin" not in request.session.keys():
            return HttpResponseRedirect("/user_login")
        user = User_table.objects.get(email_id=request.session["user_email"])
        return render(request, self.template_name, {"user": user})

    def post(self, request):
        user = User_table.objects.get(email_id=request.session["user_email"])
        user_password = request.POST.get("current-pwd")
        user_new_password = request.POST.get("new-pwd")
        user_confirm_password = request.POST.get("confirm-pwd")
        user_first_name = request.POST.get("first-name")
        user_last_name = request.POST.get("last-name")
        if user_password != user.password:
            return render(
                request,
                self.template_name,
                {"user": user, "message": "You entered wrong password!"},
            )
        if user_new_password != user_confirm_password:
            return render(
                request,
                self.template_name,
                {
                    "user": user,
                    "message": "New Password and Confirm password does not match!",
                },
            )
        user.first_name = user_first_name
        user.last_name = user_last_name
        user.password = user_new_password
        user.save()
        return render(
            request,
            self.template_name,
            {"user": user, "message": "Your account has been updated successfully!"},
        )


def sortLowToHigh(all_objects):
    return all_objects.order_by("price")


def sortHighToLow(all_objects):
    return all_objects.order_by("-price")


def getConversionRate(request):
    if request.method == "GET":
        latest_rate = ConversionRate.objects.all().order_by("-id").first()
        latest_rate = ConversionRateSerializer(latest_rate).data
        return JsonResponse(latest_rate, safe=False, status=200)
    return JsonResponse({}, safe=False, status=400)


def get_youtube_id(product):
    try:
        pattern = r'<iframe .* src="[^"]*/([^"]+)"'
        search = re.search(pattern, product.media.video_embed_link)
        youtube_video_id = search[1]
    except:
        youtube_video_id = None
    return youtube_video_id


def get_Jewellery_with_stockid(stock_id):
    try:
        product = Inventoryofjewellery.objects.select_related("media").get(
            stockid=stock_id, frontend=True
        )
    except:
        product = None
    return product


def get_diamond_with_stockid(stock_id):
    try:
        product = Inventoryofdiamond.objects.select_related("media").get(
            stockid=stock_id, frontend=True
        )
    except:
        product = None
    return product


def get_colorstone_with_stockid(stock_id):
    try:
        product = Inventoryofcolorstones.objects.select_related("media").get(
            stockid=stock_id, frontend=True
        )
    except:
        product = None
    return product


def get_jewellery_with_keyword(keyword):
    try:
        product = Inventoryofjewellery.objects.select_related("media").filter(
            Q(jewellery_type__jewel__icontains=keyword)
            | Q(center_stone__stone__icontains=keyword)
            | Q(color_of_center_stone__color__icontains=keyword)
            | Q(shape__shape__icontains=keyword)
            | Q(metal__metal__icontains=keyword),
            frontend=True,
        )
    except:
        product = None
    return product


def get_diamond_with_keyword(keyword):
    try:
        product = Inventoryofdiamond.objects.select_related("media").filter(
            Q(shape__shape__icontains=keyword)
            | Q(color_origin1__c_o__icontains=keyword)
            | Q(clarity__clarity__icontains=keyword)
            | Q(cut__cut__icontains=keyword)
            | Q(polish__polish__icontains=keyword)
            | Q(symmetry__symmetry__icontains=keyword),
            frontend=True,
        )
    except:
        product = None
    return product


def get_colorstone_with_keyword(keyword):
    try:
        product = Inventoryofcolorstones.objects.select_related("media").filter(
            Q(shape__shape__icontains=keyword)
            | Q(gem_type__gem__icontains=keyword)
            | Q(origin__org__icontains=keyword)
            | Q(treatment__treatment__icontains=keyword)
            | Q(color__color__icontains=keyword)
            | Q(lab__lab__icontains=keyword),
            frontend=True,
        )
    except:
        product = None
    return product


def SearchForUser(request):
    search_keyword = request.GET.get("search_keyword")
    search_keyword = search_keyword.lower()
    if search_keyword.startswith("j-"):
        product = get_Jewellery_with_stockid(search_keyword.capitalize())
        if product:

            return render(
                request,
                "jewellery_templates/jewellery_product_page.html",
                {
                    "product": product,
                    "user": User_table.objects.get(
                        email_id=request.session["user_email"]
                    ),
                    "youtube_video_id": get_youtube_id(product),
                },
            )
        else:
            return render(request, "404.html")
    if search_keyword.startswith("d-"):
        product = get_diamond_with_stockid(search_keyword.capitalize())
        if product:
            return render(
                request,
                "diamond_templates/diamond_product_page.html",
                {
                    "product": product,
                    "user": User_table.objects.get(
                        email_id=request.session["user_email"]
                    ),
                    "youtube_video_id": get_youtube_id(product),
                },
            )
        else:
            return render(request, "404.html")
    if search_keyword.startswith("c-"):
        product = get_colorstone_with_stockid(search_keyword.capitalize())
        if product:
            return render(
                request,
                "colorstone_templates/colorstone_product_page.html",
                {
                    "product": product,
                    "user": User_table.objects.get(
                        email_id=request.session["user_email"]
                    ),
                    "youtube_video_id": get_youtube_id(product),
                },
            )
        else:
            return render(request, "404.html")

    else:
        all_jewellery_with_keyword = get_jewellery_with_keyword(search_keyword)
        all_diamond_with_keyword = get_diamond_with_keyword(search_keyword)
        all_colorstone_with_keyword = get_colorstone_with_keyword(search_keyword)
        return render(
            request,
            "search_result.html",
            {
                "all_jewellery_with_keyword": all_jewellery_with_keyword,
                "all_diamond_with_keyword": all_diamond_with_keyword,
                "all_colorstone_with_keyword": all_colorstone_with_keyword,
                "user": User_table.objects.get(email_id=request.session["user_email"]),
            },
        )


def custom_404(request):
    return render(request, "404.html")
