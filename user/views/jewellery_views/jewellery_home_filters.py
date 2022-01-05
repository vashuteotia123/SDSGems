
from django.contrib.messages.api import MessageFailure
from django.core import paginator
from django.views.generic import View
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.utils.regex_helper import Group
from django.views.generic.base import TemplateView

from firstapp.models import *
from user.models import *
from user.forms import *
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
from django.contrib import messages
from django.template.loader import get_template


def allJewellery(request, page=1):
    all_objects = Inventoryofjewellery.objects.filter(frontend=True).all()
    paginator = Paginator(all_objects, 12)
    try:
        all_objects = paginator.page(page)
    except:
        all = paginator.page(1)
    context = {
        "all_objects": all_objects,
    }
    return render(request, 'jewellery_shop_list.html', context=context)


def JewelleryByCenterStoneFilter(request, center_stone_id, page=1):
    all_objects = Inventoryofjewellery.objects.filter(
        center_stone=center_stone_id, frontend=True).all()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
    }
    return render(request, 'jewellery_shop_list.html', context=context)


def JewelleryByMetalFilter(request, metal_id, page=1):
    all_objects = Inventoryofjewellery.objects.filter(
        metal=metal_id, frontend=True).all()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)

    context = {
        "all_objects": all_objects,
    }
    return render(request, 'jewellery_shop_list.html', context=context)


def JewelleryByJewelleryTypeFilter(request, jewellery_type_id, page=1):
    all_objects = Inventoryofjewellery.objects.filter(
        jewellery_type=jewellery_type_id, frontend=True).all()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
    }
    return render(request, 'jewellery_shop_list.html', context=context)
