from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import request
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
from firstapp.models import cut as diamondcuts  # import cut as diamondcuts
from firstapp.models import polish as diamondpolish
from firstapp.models import symmetry as diamondsymmrtry
from django.utils.decorators import method_decorator


class diamondFilter(ListView):
    template_name = "diamond_templates/diamonds_shop_list.html"

    paginate_by = 12
    model = Inventoryofdiamond

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_diaobjects = self.get_queryset()
        diamondShapes = shape_d.objects.all()
        diamondCuts = diamondcuts.objects.all()
        diamondColorOrigin = color_origin.objects.all()
        diamondFluorescenceColors = fluorescence_color.objects.all()
        diamondPolishes = diamondpolish.objects.all()
        diamondSymmetrys = diamondsymmrtry.objects.all()
        diamondFluoresceneIntensitys = fluorescence_intensity.objects.all()
        context['diamondshapes'] = diamondShapes
        context['diamondcuts'] = diamondCuts
        context['diamondcolororigin'] = diamondColorOrigin
        context['diamondpolishes'] = diamondPolishes
        context['diamondsymmetrys'] = diamondSymmetrys
        context['diamondfluorescencecolors'] = diamondFluorescenceColors
        context['diamondfluorescenceintensitys'] = diamondFluoresceneIntensitys
        context['user'] = self.get_user()
        context['shapes'] = SafeString(str([]))
        context['cuts'] = SafeString(str([]))
        context['colororigins'] = SafeString(str([]))
        context['polishes'] = SafeString(str([]))
        context['symmetrys'] = SafeString(str([]))
        context['fluorescencecolors'] = SafeString(str([]))
        context['fluorescenceintensitys'] = SafeString(str([]))
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
        if self.request.GET.get('polish'):
            all_diaobjects, polish = self.get_by_polish(
                self.request.GET.get('polish'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            polishes = []
            polishes.append(polish)
            context['polishes'] = SafeString(str(polishes))
            context['all_diaobjects'] = all_diaobjects
            return context
        if self.request.GET.get('symmetry'):
            all_diaobjects, symmetry = self.get_by_symmetry(
                self.request.GET.get('symmetry'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            symmetrys = []
            symmetrys.append(symmetry)
            context['symmetrys'] = SafeString(str(symmetrys))
            context['all_diaobjects'] = all_diaobjects
            return context
        if self.request.GET.get('fluorescencecolor'):
            all_diaobjects, fluorescencecolor = self.get_by_fluorescencecolor(
                self.request.GET.get('fluorescencecolor'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            fluorescencecolors = []
            fluorescencecolors.append(fluorescencecolor)
            context['fluorescencecolors'] = SafeString(str(fluorescencecolors))
            context['all_diaobjects'] = all_diaobjects
            return context
        if self.request.GET.get('fluorescenceintensity'):
            all_diaobjects, fluorescenceintensity = self.get_by_fluorescenceintensity(
                self.request.GET.get('fluorescenceintensity'), all_diaobjects)
            context['total_count'] = self.get_object_count(all_diaobjects)
            paginator = Paginator(all_diaobjects, self.paginate_by)
            page = self.request.GET.get('page')
            if page:
                all_diaobjects = paginator.get_page(page)
            else:
                all_diaobjects = paginator.get_page(1)
            fluorescenceintensitys = []
            fluorescenceintensitys.append(fluorescenceintensity)
            context['fluorescenceintensitys'] = SafeString(
                str(fluorescenceintensitys))
            context['all_diaobjects'] = all_diaobjects

        all_diaobjects, shapes = self.get_shape_filtered(all_diaobjects)
        all_diaobjects, cuts = self.get_cut_filtered(all_diaobjects)
        all_diaobjects, colororigins = self.get_colororigin_filtered(
            all_diaobjects)
        all_diaobjects, polishes = self.get_polish_filtered(all_diaobjects)
        all_diaobjects, symmetrys = self.get_symmetry_filtered(all_diaobjects)
        all_diaobjects, fluorescencecolors = self.get_fluorescencecolor_filtered(
            all_diaobjects)
        all_diaobjects, fluorescenceintensitys = self.get_fluorescenceintensity_filtered(
            all_diaobjects)
        all_diaobjects, hightolow = self.get_high_to_low(all_diaobjects)
        all_diaobjects, lowtohigh = self.get_low_to_high(all_diaobjects)
        context['total_count'] = self.get_object_count(all_diaobjects)
        paginator = Paginator(all_diaobjects, self.paginate_by)
        page = self.request.GET.get('page')
        if page:
            all_diaobjects = paginator.get_page(page)
        else:
            all_diaobjects = paginator.get_page(1)

        if (lowtohigh == 1):
            context['LowToHigh'] = 1

        if hightolow == 1:
            context['HighToLow'] = 1

        context['all_diaobjects'] = all_diaobjects
        context['shapes'] = SafeString(str(shapes))
        context['cuts'] = SafeString(str(cuts))
        context['colororigins'] = SafeString(str(colororigins))
        context['polishes'] = SafeString(str(polishes))
        context['symmetrys'] = SafeString(str(symmetrys))
        context['fluorescencecolors'] = SafeString(str(fluorescencecolors))
        context['fluorescenceintensitys'] = SafeString(
            str(fluorescenceintensitys))
        return context

    def get_queryset(self):
        return super().get_queryset().filter(frontend=True).all()

    def get_user(self):
        if 'user_email' in self.request.session.keys():
            return User_table.objects.get(email_id=self.request.session['user_email'])
        return None

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

    def get_polish_filtered(self, all_diaobjects):
        polishes = self.request.GET.getlist('polishes[]')
        if(len(polishes) > 0):
            all_diaobjects = all_diaobjects.filter(
                polish__polish__in=polishes)
        return all_diaobjects, polishes

    def get_symmetry_filtered(self, all_diaobjects):
        symmetrys = self.request.GET.getlist('symmetrys[]')
        if(len(symmetrys) > 0):
            all_diaobjects = all_diaobjects.filter(
                symmetry__symmetry__in=symmetrys)
        return all_diaobjects, symmetrys

    def get_fluorescencecolor_filtered(self, all_diaobjects):
        fluorescenceColors = self.request.GET.getlist('fluorescenceColors[]')
        if(len(fluorescenceColors) > 0):
            all_diaobjects = all_diaobjects.filter(
                fluorescence_color__f_color__in=fluorescenceColors)
        return all_diaobjects, fluorescenceColors

    def get_fluorescenceintensity_filtered(self, all_diaobjects):
        fluorescenceIntensitys = self.request.GET.getlist(
            'fluorescenceIntensitys[]')
        if(len(fluorescenceIntensitys) > 0):
            all_diaobjects = all_diaobjects.filter(
                fluorescence_intensity__f_intensity__in=fluorescenceIntensitys)
        return all_diaobjects, fluorescenceIntensitys

    def get_by_shape(self, shape, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(shape__shape=shape)
        return all_diaobjects, shape

    def get_by_cut(self, cut, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(cut__cut=cut)
        return all_diaobjects, cut

    def get_by_colororigin(self, colororigin, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(color_origin1__c_o=colororigin)
        return all_diaobjects, colororigin

    def get_by_polish(self, polish, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(polish__polish=polish)
        return all_diaobjects, polish

    def get_by_symmetry(self, symmetry, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(symmetry__symmetry=symmetry)
        return all_diaobjects, symmetry

    def get_by_fluorescencecolor(self, fluorescencecolor, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(
            fluorescence_color__f_color=fluorescencecolor)
        return all_diaobjects, fluorescencecolor

    def get_by_fluorescenceintensity(self, fluorescenceintensity, all_diaobjects):
        all_diaobjects = all_diaobjects.filter(
            fluorescence_intensity__f_intensity=fluorescenceintensity)
        return all_diaobjects, fluorescenceintensity

    def get_object_count(self, all_diaobjects):
        return all_diaobjects.count()

    def get_high_to_low(self, all_diaobjects):
        HighToLow = self.request.GET.getlist('HighToLow[]')
        if len(HighToLow) > 0:
            return all_diaobjects.order_by('-tag_price_d'), 1
        return all_diaobjects, 0

    def get_low_to_high(self, all_diaobjects):
        LowToHigh = self.request.GET.getlist('LowToHigh[]')
        if len(LowToHigh) > 0:
            return all_diaobjects.order_by('tag_price_d'), 1
        return all_diaobjects, 0
