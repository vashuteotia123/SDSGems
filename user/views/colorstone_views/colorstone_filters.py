from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.utils import safestring
from firstapp.models import *
from user.models import *
from django.shortcuts import *
from user.views.common_views import *
import random
import re
from django.views.generic import ListView
import json
from django.utils.safestring import SafeString


class colorStoneFilter(ListView):
    template_name = "colorstone_templates/colorstone_shop_list.html"

    paginate_by = 12
    model = Inventoryofcolorstones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_objects = self.get_queryset()
        # Loading common filters
        colorStoneShapes = shape_cs.objects.all()
        colorStoneColors = color_of_colorstone.objects.all()
        colorStoneOrigins = Origin_cs.objects.all()
        colorStoneGemTypes = gemtype.objects.all()
        context['colorStoneShapes'] = colorStoneShapes
        context['colorStoneColors'] = colorStoneColors
        context['colorStoneOrigins'] = colorStoneOrigins
        context['colorStoneGemTypes'] = colorStoneGemTypes
        context['user'] = self.get_user()
        context['colors'] = SafeString(str([]))
        context['shapes'] = SafeString(str([]))
        context['origins'] = SafeString(str([]))
        context['gemtypes'] = SafeString(str([]))

        # Handling Navigation Bar Filter Requests
        if self.request.GET.get('shape'):
            all_objects, shape = self.get_by_shape(
                self.request.GET.get('shape'), all_objects)
            context['total_count'] = self.get_object_count(all_objects)
            paginator = Paginator(all_objects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_objects = paginator.get_page(page)
            else:
                all_objects = paginator.get_page(1)
            shapes = []
            shapes.append(shape)
            context['shapes'] = SafeString(str(shapes))
            context['all_objects'] = all_objects
            return context  # return context

        if self.request.GET.get('color'):
            all_objects, color = self.get_by_color(
                self.request.GET.get('color'), all_objects)
            context['total_count'] = self.get_object_count(all_objects)
            paginator = Paginator(all_objects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_objects = paginator.get_page(page)
            else:
                all_objects = paginator.get_page(1)

            colors = self.request.GET.getlist('color')
            context['colors'] = SafeString(str(colors))
            context['all_objects'] = all_objects
            return context

        if self.request.GET.get('origin'):
            all_objects, origin = self.get_by_origin(
                self.request.GET.get('origin'), all_objects)
            context['total_count'] = self.get_object_count(all_objects)
            paginator = Paginator(all_objects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_objects = paginator.get_page(page)
            else:
                all_objects = paginator.get_page(1)
            origins = []
            origins.append(origin)
            context['origins'] = SafeString(str(origins))
            context['all_objects'] = all_objects
            return context

        if self.request.GET.get('gemtype'):
            all_objects, gem = self.get_by_gemtype(
                self.request.GET.get('gemtype'), all_objects)
            context['total_count'] = self.get_object_count(all_objects)
            paginator = Paginator(all_objects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_objects = paginator.get_page(page)
            else:
                all_objects = paginator.get_page(1)
            gemtypes = []
            gemtypes.append(gem)
            context['gemtypes'] = SafeString(str(gemtypes))
            context['all_objects'] = all_objects
            return context

        # Handling on page Filters
        all_objects, shapes = self.get_shape_filtered(all_objects)
        all_objects, colors = self.get_color_filtered(all_objects)
        all_objects, origins = self.get_origin_filtered(all_objects)
        all_objects, gemtypes = self.get_gemtype_filtered(all_objects)
        context['total_count'] = self.get_object_count(all_objects)
        paginator = Paginator(all_objects, self.paginate_by)
        page = self.request.GET.get('page')
        if page:
            all_objects = paginator.get_page(page)
        else:
            all_objects = paginator.get_page(1)

        context['all_objects'] = all_objects
        context['shapes'] = SafeString(str(shapes))
        context['colors'] = SafeString(str(colors))
        context['origins'] = SafeString(str(origins))
        context['gemtypes'] = SafeString(str(gemtypes))
        return context

    def get_queryset(self):
        return super().get_queryset().select_related('media').filter(frontend=True).all().order_by('-id')

    def get_user(self):
        if 'user_email' in self.request.session.keys():
            return User_table.objects.get(
                email_id=self.request.session['user_email'])
        return None

    def get_shape_filtered(self, all_objects):
        shapes = self.request.GET.getlist('shapes[]')
        if len(shapes) > 0:
            all_objects = all_objects.filter(shape__shape__in=shapes)

        return all_objects, shapes

    def get_color_filtered(self, all_objects):
        colors = self.request.GET.getlist('colors[]')
        if len(colors) > 0:
            all_objects = all_objects.filter(color__color__in=colors)
        return all_objects, colors

    def get_origin_filtered(self, all_objects):
        origins = self.request.GET.getlist('origins[]')
        if len(origins) > 0:
            all_objects = all_objects.filter(
                origin__org__in=origins)
        return all_objects, origins

    def get_gemtype_filtered(self, all_objects):
        gemtypes = self.request.GET.getlist('gemtypes[]')
        if len(gemtypes) > 0:
            all_objects = all_objects.filter(
                gem_type__gem__in=gemtypes)
        return all_objects, gemtypes

    def get_by_shape(self, shape, all_objects):
        all_objects = all_objects.filter(shape__shape=shape)
        return all_objects, shape

    def get_by_color(self, color, all_objects):
        all_objects = all_objects.filter(color__color=color)
        return all_objects, color

    def get_by_origin(self, origin, all_objects):
        all_objects = all_objects.filter(origin__org=origin)
        return all_objects, origin

    def get_by_gemtype(self, gemtype, all_objects):
        all_objects = all_objects.filter(gem_type__gem=gemtype)
        return all_objects, gemtype

    def get_object_count(self, all_objects):
        return all_objects.count()
