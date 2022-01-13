from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.utils import safestring
from firstapp.models import *
from firstapp.models import centerstone as jewellerycenterstone
from user.models import *
from django.shortcuts import *
from user.views.common_views import *
import random
import re
from django.views.generic import ListView
import json
from django.utils.safestring import SafeString


class jewelleryFilter(ListView):
    template_name = "jewellery_templates/jewellery_shop_list.html"
    paginate_by = 12
    model = Inventoryofjewellery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_jewobjects = self.get_queryset()
        jewelleryMetal = metal1.objects.all()
        jewelleryType = jewell.objects.all()
        jewelleryCenterStone = jewellerycenterstone.objects.all()
        jewelleryColorofCenterStone = colorofcstone.objects.all()
        jewelleryShape = shape1.objects.all()
        context['jewellerymetal'] = jewelleryMetal
        context['jewellerytype'] = jewelleryType
        context['jewellerycenterstone'] = jewelleryCenterStone
        context['jewelleryshape'] = jewelleryShape
        context['jewellerycolorofcenterstone'] = jewelleryColorofCenterStone
        context['user'] = self.get_user()
        context['shapes'] = SafeString(str([]))
        context['types'] = SafeString(str([]))
        context['metals'] = SafeString(str([]))
        context['centerstones'] = SafeString(str([]))
        context['colorofcenterstones'] = SafeString(str([]))
        if self.request.GET.get('shape'):
            all_jewobjects, shape = self.get_by_shape(
                self.request.GET.get('shape'), all_jewobjects)
            context['total_count'] = self.get_object_count(all_jewobjects)
            paginator = Paginator(all_jewobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_jewobjects = paginator.get_page(page)
            else:
                all_jewobjects = paginator.get_page(1)
            shapes = []
            shapes.append(shape)
            context['shapes'] = SafeString(str(shapes))
            context['all_jewobjects'] = all_jewobjects
            return context  # return context
        if self.request.GET.get('typej'):
            all_jewobjects, typej = self.get_by_type(
                self.request.GET.get('typej'), all_jewobjects)
            context['total_count'] = self.get_object_count(all_jewobjects)
            paginator = Paginator(all_jewobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_jewobjects = paginator.get_page(page)
            else:
                all_jewobjects = paginator.get_page(1)
            types = []
            types.append(typej)
            context['types'] = SafeString(str(types))
            context['all_jewobjects'] = all_jewobjects
            return context
        if self.request.GET.get('metal'):
            all_jewobjects, metal = self.get_by_metal(
                self.request.GET.get('metal'), all_jewobjects)
            context['total_count'] = self.get_object_count(all_jewobjects)
            paginator = Paginator(all_jewobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_jewobjects = paginator.get_page(page)
            else:
                all_jewobjects = paginator.get_page(1)
            metals = []
            metals.append(metal)
            context['metals'] = SafeString(str(metals))
            context['all_jewobjects'] = all_jewobjects
            return context
        if self.request.GET.get('centerstone'):
            all_jewobjects, centerstone = self.get_by_centerstone(
                self.request.GET.get('centerstone'), all_jewobjects)
            context['total_count'] = self.get_object_count(all_jewobjects)
            paginator = Paginator(all_jewobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_jewobjects = paginator.get_page(page)
            else:
                all_jewobjects = paginator.get_page(1)
            centerstones = []
            centerstones.append(centerstone)
            context['centerstones'] = SafeString(str(centerstones))
            context['all_jewobjects'] = all_jewobjects
            return context
        if self.request.GET.get('colorofcenterstone'):
            all_jewobjects, colorofcenterstone = self.get_by_colorofcenterstone(
                self.request.GET.get('colorofcenterstone'), all_jewobjects)
            context['total_count'] = self.get_object_count(all_jewobjects)
            paginator = Paginator(all_jewobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_jewobjects = paginator.get_page(page)
            else:
                all_jewobjects = paginator.get_page(1)
            colorofcenterstones = []
            colorofcenterstones.append(colorofcenterstone)
            context['colorofcenterstones'] = SafeString(
                str(colorofcenterstones))
            context['all_jewobjects'] = all_jewobjects
            return context
        all_jewobjects, shapes = self.get_shape_filtered(all_jewobjects)
        all_jewobjects, types = self.get_type_filtered(all_jewobjects)
        all_jewobjects, metals = self.get_metal_filtered(all_jewobjects)
        all_jewobjects, centerstones = self.get_centerstone_filtered(
            all_jewobjects)
        all_jewobjects, colorofcenterstones = self.get_colorofcenterstone_filtered(
            all_jewobjects)
        all_jewobjects, hightolow = self.get_high_to_low(all_jewobjects)
        all_jewobjects, lowtohigh = self.get_low_to_high(all_jewobjects)
        context['total_count'] = self.get_object_count(all_jewobjects)
        paginator = Paginator(all_jewobjects, self.paginate_by)
        page = self.request.GET.get('page')
        if page:
            all_jewobjects = paginator.get_page(page)
        else:
            all_jewobjects = paginator.get_page(1)
        if (lowtohigh == 1):
            context['LowToHigh'] = 1

        if hightolow == 1:
            context['HighToLow'] = 1

        context['all_jewobjects'] = all_jewobjects
        context['shapes'] = SafeString(str(shapes))
        context['types'] = SafeString(str(types))
        context['metals'] = SafeString(str(metals))
        context['centerstones'] = SafeString(str(centerstones))
        context['colorofcenterstones'] = SafeString(str(colorofcenterstones))
        return context

    def get_queryset(self):
        return super().get_queryset().filter(frontend=True).all()

    def get_user(self):
        try:
            user = User_table.objects.get(email_id=self.request.session['user_email'])
        except:
            user = None 
        return user

    def get_shape_filtered(self, all_jewobjects):
        shapes = self.request.GET.getlist('shapes[]')
        if(len(shapes) > 0):
            all_jewobjects = all_jewobjects.filter(shape__shape__in=shapes)
        return all_jewobjects, shapes

    def get_metal_filtered(self, all_jewobjects):
        metals = self.request.GET.getlist('metals[]')
        if(len(metals) > 0):
            all_jewobjects = all_jewobjects.filter(metal__metal__in=metals)
        return all_jewobjects, metals

    def get_centerstone_filtered(self, all_jewobjects):
        centerstones = self.request.GET.getlist('centerstones[]')
        if(len(centerstones) > 0):
            all_jewobjects = all_jewobjects.filter(
                center_stone__stone__in=centerstones)
        return all_jewobjects, centerstones

    def get_type_filtered(self, all_jewobjects):
        types = self.request.GET.getlist('types[]')
        if(len(types) > 0):
            all_jewobjects = all_jewobjects.filter(
                jewellery_type__jewel__in=types)
        return all_jewobjects, types

    def get_colorofcenterstone_filtered(self, all_jewobjects):
        colorofcenterstones = self.request.GET.getlist('colorofcenterstones[]')
        if(len(colorofcenterstones) > 0):
            all_jewobjects = all_jewobjects.filter(
                color_of_center_stone__color__in=colorofcenterstones)
        return all_jewobjects, colorofcenterstones

    def get_by_shape(self, shape, all_jewobjects):
        all_jewobjects = all_jewobjects.filter(shape__shape=shape)
        return all_jewobjects, shape

    def get_by_type(self, typej, all_jewobjects):
        all_jewobjects = all_jewobjects.filter(jewellery_type__jewel=typej)
        return all_jewobjects, typej

    def get_by_metal(self, metal, all_jewobjects):
        all_jewobjects = all_jewobjects.filter(metal__metal=metal)
        return all_jewobjects, metal

    def get_by_centerstone(self, centerstone, all_jewobjects):
        all_jewobjects = all_jewobjects.filter(center_stone__stone=centerstone)
        return all_jewobjects, centerstone

    def get_by_colorofcenterstone(self, colorofcenterstone, all_jewobjects):
        all_jewobjects = all_jewobjects.filter(
            color_of_center_stone__color=colorofcenterstone)
        return all_jewobjects, colorofcenterstone

    def get_object_count(self, all_jewobjects):
        return all_jewobjects.count()

    def get_high_to_low(self, all_jewobjects):
        HighToLow = self.request.GET.getlist('HighToLow[]')
        if len(HighToLow) > 0:
            return all_jewobjects.order_by('-tag_price'), 1
        return all_jewobjects, 0

    def get_low_to_high(self, all_jewobjects):
        LowToHigh = self.request.GET.getlist('LowToHigh[]')
        if len(LowToHigh) > 0:
            return all_jewobjects.order_by('tag_price'), 1
        return all_jewobjects, 0
