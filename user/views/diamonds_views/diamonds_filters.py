from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.utils import safestring
from firstapp.models import *
from user.models import *
from django.shortcuts import *
from user.views.diamonds_views.diamonds_home_filters import allDiamonds
from user.views.common_views import *
import random
import re
from django.views.generic import ListView
import json
from django.utils.safestring import SafeString


class diamondFilter(ListView):
    template_name = "diamond_templates/diamonds_shop_list1.html"
    diamondshapes = shape_d.objects.all()
    diamondcuts = cut.objects.all()
    diamondcolororigin = color_origin.objects.all()

    paginate_by = 12
    model = Inventoryofdiamond

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_diaobjects = self.get_queryset()
        context['diamondshapes'] = self.diamondshapes
        context['diamondcuts'] = self.diamondcuts
        context['diamondcolororigin'] = self.diamondcolororigin
        context['user'] = self.get_user()
        context['shapes'] = SafeString(str([]))
        context['cuts'] = SafeString(str([]))
        context['colororigins'] = SafeString(str([]))
        if self.request.GET.get('shape'):
            all_diaobjects, shape = self.get_by_shape(
                self.request.GET.get('shape'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            shapes = []
            shapes.append(shape)
            context['shapes'] = SafeString(str(shapes))
            context['all_diaobjects'] = all_diaobjects
            return context  # return context
        if self.request.GET.get('cut'):
            all_diaobjects, cut = self.get_by_cut(
                self.request.GET.get('cut'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            cuts = self.request.GET.getlist('cut')
            context['cuts'] = SafeString(str(cuts))
            context['all_diaobjects'] = all_diaobjects
            return context
        if self.request.GET.get('colororigin'):
            all_diaobjects, colororigin = self.get_by_colororigin(
                self.request.GET.get('colororigin'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            colororigins = []
            colororigins.append(colororigin)
            context['colororigins'] = SafeString(str(colororigins))
            context['all_diaobjects'] = all_diaobjects
            return context
        all_diaobjects, shapes = self.get_shape_filtered(all_diaobjects)
        all_diaobjects, cuts = self.get_cut_filtered(all_diaobjects)
        all_diaobjects, colororigins = self.get_colororigin_filtered(
            all_diaobjects)
        context['total_count'] = self.get_object_count(all_diaobjects)
        paginator = Paginator(all_diaobjects, self.paginate_by)
        page = self.request.GET.get('page')
        if page:
            all_diaobjects = paginator.get_page(page)
        else:
            all_diaobjects = paginator.get_page(1)

        context['all_diaobjects'] = all_diaobjects
        context['shapes'] = SafeString(str(shapes))
        context['cuts'] = SafeString(str(cuts))
        context['colororigins'] = SafeString(str(colororigins))
        return context

    def get_queryset(self):
        return super().get_queryset().filter(frontend=True).all().order_by('-id')

    def get_user(self):
        user = User_table.objects.get(
            email_id=self.request.session['user_email'])
        return user

    def get_shape_filtered(self, all_diaobjects):
        shapes = self.request.GET.getlist('shapes[]')
        if(len(shapes) > 0):
            all_diaobjects = all_diaobjects.filter(shape__shape__in=shapes)
        return all_diaobjects, shapes

    def get_cut_filtered(self, all_diaobjects):
        cuts = self.request.GET.getlist('cuts[]')
        if(len(cuts) > 0):
            all_diaobjects = all_diaobjects.filter(cut__cut__in=cuts)
        return all_diaobjects, cuts

    def get_colororigin_filtered(self, all_diaobjects):
        colororigins = self.request.GET.getlist('colororigins[]')
        if(len(colororigins) > 0):
            all_diaobjects = all_diaobjects.filter(
                color_origin1__c_o__in=colororigins)
        return all_diaobjects, colororigins

    def get_by_shape(self, shape, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(shape__shape=shape)
        return all_diaobjects, shape

    def get_by_cut(self, cut, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(cut__cut=cut)
        return all_diaobjects, cut

    def get_by_colororigin(self, colororigin, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(color_origin1__c_o=colororigin)
        return all_diaobjects, colororigin

    def get_object_count(self, all_diaobjects):
        return all_diaobjects.count()
