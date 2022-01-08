
from django.contrib.messages.api import MessageFailure
from django.core import paginator
from django.http import response
from django.views.generic import View
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.utils.regex_helper import Group
from django.views.generic.base import TemplateView

from firstapp.models import ColorStone_media, Inventoryofcolorstones
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

from user.views.common_views import myuser_login_required, user_login


@myuser_login_required
def allColorStones(request, page=1):
    all_objects = Inventoryofcolorstones.objects.select_related(
        'media').filter(frontend=True).all().order_by('-id')
    total_count = all_objects.count()
    paginator = Paginator(all_objects, 12)
    try:
        all_objects = paginator.page(page)
    except:
        all_objects = paginator.page(1)
    context = {
        "all_objects": all_objects,
        "total_count": total_count,
        "current_url": "allColorStones",
        "user": User_table.objects.get(pk=request.session['user_email']),
    }
    return render(request, 'colorstone_templates/colorstone_shop_list.html', context=context)


@ myuser_login_required
def colorStoneByShapeFilter(request, shape_id, page=1):
    all_objects = Inventoryofcolorstones.objects.select_related('media').filter(
        shape=shape_id, frontend=True).all().order_by('-id')
    total_count = all_objects.count()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
        "total_count": total_count,
        "current_url": "colorStoneByShapeFilter",
        "user": User_table.objects.get(pk=request.session['user_email']),
        "shape_id": shape_id,
    }
    return render(request, 'colorstone_templates/colorStoneByShapeFilter.html', context=context)


@ myuser_login_required
def colorStoneGemTypeFilter(request, gemtype_id, page=1):
    all_objects = Inventoryofcolorstones.objects.select_related('media').filter(
        gem_type=gemtype_id, frontend=True).all().order_by('-id')
    total_count = all_objects.count()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
        "total_count": total_count,
        "current_url": "colorStoneGemTypeFilter",
        "user": User_table.objects.get(pk=request.session['user_email']),
        "gemtype_id": gemtype_id,
    }
    return render(request, 'colorstone_templates/colorStoneGemTypeFilter.html', context=context)


@ myuser_login_required
def colorStoneByOriginFilter(request, origin_id, page=1):
    all_objects = Inventoryofcolorstones.objects.select_related('media').filter(
        origin=origin_id, frontend=True).all().order_by('-id')
    total_count = all_objects.count()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
        "total_count": total_count,
        "current_url": "colorStoneByOriginFilter",
        "origin_id": origin_id,
        "user": User_table.objects.get(pk=request.session['user_email']),
    }
    return render(request, 'colorstone_templates/colorStoneByOriginFilter.html', context=context)


@ myuser_login_required
def colorStoneByColourFilter(request, colour_id, page=1):
    all_objects = Inventoryofcolorstones.objects.select_related('media').filter(
        color=colour_id, frontend=True).all().order_by('-id')
    total_count = all_objects.count()
    paginator = Paginator(all_objects, 12)
    all_objects = paginator.page(page)
    context = {
        "all_objects": all_objects,
        "total_count": total_count,
        "current_url": "colorStoneByColourFilter",
        "colour_id": colour_id,
        "user": User_table.objects.get(pk=request.session['user_email']),
    }
    return render(request, 'colorstone_templates/colorStoneByColourFilter.html', context=context)


def custom_404(request):
    return render(request, '404.html')
