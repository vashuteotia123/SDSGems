from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
# Register your models here.
from django.shortcuts import redirect
from django_object_actions import DjangoObjectActions
from django.forms import TextInput, Textarea
from django.contrib import messages


# Dev mode
development_mode = False

# doploy variables
deploy_color_stone = True
deploy_jewellery = False
deploy_diamond = False


@admin.register(State)
class stateadmin(admin.ModelAdmin):
    pass


@admin.register(User_table)
class usertableadmin(admin.ModelAdmin):
    pass


if deploy_color_stone:
    @admin.register(countries)
    class CountryAdmin(ImportExportModelAdmin):
        pass

    @admin.register(Treatment_cs)
    class treatcsadmin(ImportExportModelAdmin):
        # def HomePage(treatcsadmin, request, queryset):
        #         return redirect('/index')

        # HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
        # changelist_actions = ('HomePage',)
        pass

    @admin.register(Origin_cs)
    class originadmin(ImportExportModelAdmin):
        def HomePage(originadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(Lab_cs)
    class labadmin(ImportExportModelAdmin):
        def HomePage(labadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(shape_cs)
    class shapeadmin(ImportExportModelAdmin):
        def HomePage(shapeadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(companyinfo)
    class CompanyAdmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(CompanyAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        actions = ['change_name']
        changelist_actions = ('HomePage',)
        search_fields = ['company_name', 'email']
        list_display_links = ['company_name']
        # list_editable = ['company_name']
        list_display = [f.name for f in companyinfo._meta.fields]

        def response_change(self, request, obj):
            return redirect('/index')

        def response_add(self, request, obj, post_url_continue=None):
            return redirect('/index')

    @admin.register(ColorStone_media)
    class ColorStone_media_admin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(ColorStone_media_admin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)
        list_display = [entry.name for entry in ColorStone_media._meta.fields]

        def response_change(self, request, obj=None):
            messages.success(request, "Media successfully changed!")
            return redirect('/index')

        def response_add(self, request, obj=None):
            messages.success(request, "Media successfully added!")
            return redirect('/index')

    @admin.register(Salesofcolorstones)
    class salesofcsadmin(admin.ModelAdmin):
        # def HomePage(salesofcsadmin, request, queryset):
        #     return redirect('/index')

        # HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
        # changelist_actions = ('HomePage',)

        formfield_overrides = {models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 40})}, }
        search_fields = ['company_name__company_name', 'stockid',
                         'location__place', 'gem_type__gem', 'shape__shape']
        list_editable = ['date', 'company_name', 'amount_cs', 'DIS_cs', 'DIS_amount_cs', 'total_value_cs',
                         'tag_price_cs', 'price', 'Weight_cs', 'rate_cs', 'salesapprovalstatus_cs', 'comment']
        list_display = [f.name for f in Salesofcolorstones._meta.fields]

        def has_add_permission(self, request, obj=None):
            return False

        def has_change_permission(self, request, obj=None):
            return True

        def has_delete_permission(self, request, obj=None):
            return False

    @admin.register(currencies)
    class curradmin(ImportExportModelAdmin):
        def HomePage(curradmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


if development_mode:

    # @admin.register(companyinfo)
    # class CompanyAdmin(DjangoObjectActions,admin.ModelAdmin):
    #     def HomePage(CompanyAdmin, request, queryset):
    #         return redirect('/index')

    #     HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
    #     actions = ['change_name']
    #     changelist_actions = ('HomePage',)
    #     search_fields = ['company_name', 'email']
    #     list_display_links =['company_name']
    #     # list_editable = ['company_name']
    #     list_display = [f.name for f in companyinfo._meta.fields]

    #     def response_change(self, request, obj):
    #         return redirect('/index')

    #     def response_add(self, request, obj, post_url_continue=None):
    #         return redirect('/index')

    @admin.register(POJ)
    class PurchaseOFJewell(admin.ModelAdmin):
        list_editable = ['company_name']
        list_display = [f.name for f in POJ._meta.fields]
        readonly_fields = ['total', 'discount_amount']

    @admin.register(Inventoryofjewellery)
    class iojadmin(admin.ModelAdmin):
        pass

    @admin.register(centerstone)
    class CSadmin(admin.ModelAdmin):
        pass

    @admin.register(colorofcstone)
    class COCSadmin(admin.ModelAdmin):
        pass

    @admin.register(metal1)
    class metaladmin(admin.ModelAdmin):
        pass

    @admin.register(jewell)
    class jewelladmin(admin.ModelAdmin):
        pass

    @admin.register(certificate)
    class certadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(certadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    # @admin.register(currencies)
    # class curradmin(admin.ModelAdmin):
    #     pass

    @admin.register(PurchaseOfColorStones)
    class pcosadmin(admin.ModelAdmin):
        pass

    # @admin.register(Treatment_cs)
    # class treatcsadmin(admin.ModelAdmin):
    #     pass

    # @admin.register(Origin_cs)
    # class originadmin(admin.ModelAdmin):
    #     pass

    # @admin.register(Lab_cs)
    # class labadmin(admin.ModelAdmin):
    #     pass

    # @admin.register(shape_cs)
    # class shapeadmin(admin.ModelAdmin):
    #     pass

    @admin.register(Inventoryofcolorstones)
    class inventoryofcsadmin(ImportExportModelAdmin):
        pass

    @admin.register(shape1)
    class shapeadmin(admin.ModelAdmin):
        pass

    @admin.register(POD)
    class PODadmin(admin.ModelAdmin):
        pass

    @admin.register(Inventoryofdiamond)
    class inventoryofdiamondadmin(admin.ModelAdmin):
        pass

    @admin.register(shape_d)
    class shapedadmin(admin.ModelAdmin):
        pass

    @admin.register(clarity)
    class clarityadmin(admin.ModelAdmin):
        pass

    @admin.register(color_origin)
    class color_originadmin(admin.ModelAdmin):
        pass

    @admin.register(white_color_grade)
    class white_color_gradeadmin(admin.ModelAdmin):
        pass

    @admin.register(fancy_color_intensity)
    class fancy_color_intensityadmin(admin.ModelAdmin):
        pass

    @admin.register(fancycolor_grade)
    class fancycolor_gradeadmin(admin.ModelAdmin):
        pass

    @admin.register(fluorescence_intensity)
    class fluoroscence_intensityadmin(admin.ModelAdmin):
        pass

    @admin.register(fluorescence_color)
    class fluorescence_intensityadmin(admin.ModelAdmin):
        pass

    @admin.register(certificate_d)
    class certificate_dadmin(admin.ModelAdmin):
        pass

    @admin.register(Salesofjewellery)
    class salesofjewadmin(ImportExportModelAdmin):
        search_fields = ['company_name']

        list_editable = ['company_name', ]
        list_display = [f.name for f in Salesofjewellery._meta.fields]

        def has_add_permission(self, request, obj=None):
            return False

        def has_change_permission(self, request, obj=None):
            return True

        def has_delete_permission(self, request, obj=None):
            return False

    @admin.register(cloneInvofjewellery)
    class cloneInvofjewadmin(admin.ModelAdmin):
        list_display = [
            entry.name for entry in cloneInvofjewellery._meta.fields]
        list_editable = ["tag_price", "rate"]

    @admin.register(cloneInvofcolorstones)
    class cloneInvofcsadmin(admin.ModelAdmin):
        list_display = [
            entry.name for entry in cloneInvofcolorstones._meta.fields]
        list_editable = ["tag_price_cs", "rate_cs"]

    # @admin.register(Salesofcolorstones)
    # class salesofcsadmin(DjangoObjectActions,admin.ModelAdmin):
    #     def HomePage(salesofcsadmin, request, queryset):
    #         return redirect('/index')

    #     HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
    #     changelist_actions = ('HomePage',)

    #     formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},}
    #     search_fields = ['date', 'company_name', 'stockid']
    #     list_editable = ['date','company_name', 'amount_cs','DIS_cs','DIS_amount_cs', 'total_value_cs', 'tag_price_cs', 'rate_cs', 'salesapprovalstatus_cs', 'comment']
    #     list_display = [f.name for f in Salesofcolorstones._meta.fields]
    #     def has_add_permission(self, request, obj=None):
    #         return False
    #     def has_change_permission(self, request, obj=None):
    #         return True
    #     def has_delete_permission(self, request, obj=None):
    #         return False

    @admin.register(cloneInvofdiamond)
    class cloneInvofdadmin(admin.ModelAdmin):
        list_display = [entry.name for entry in cloneInvofdiamond._meta.fields]
        list_editable = ["tag_price_d", "rate_d"]

    @admin.register(Salesofdiamond)
    class salesofdadmin(admin.ModelAdmin):
        pass

    # @admin.register(ColorStone_media)
    # class ColorStone_media_admin(admin.ModelAdmin):
    #     list_display = [entry.name for entry in ColorStone_media._meta.fields]

    #     def response_change(self, request, obj=None):
    #         messages.success(request, "Media successfully changed!")
    #         return redirect('/index')

    #     def response_add(self, request, obj=None):
    #         messages.success(request, "Media successfully added!")
    #         return redirect('/index')

    # @admin.register(Salesreturn)
    # class salesofdadmin(admin.ModelAdmin):
    #     pass


@admin.register(gemtype)
class gemtypeadmin(ImportExportModelAdmin):
    def HomePage(gemtypeadmin, request, queryset):
        return redirect('/index')

    HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
    changelist_actions = ('HomePage',)


# @admin.register(cut)
# class cutadmin(admin.ModelAdmin):
#     pass


# @admin.register(polish)
# class polishadmin(admin.ModelAdmin):
#     pass


# @admin.register(symmetry)
# class symmetryadmin(admin.ModelAdmin):
#     pass


@admin.register(location)
class LocAdmin(ImportExportModelAdmin):
    def HomePage(LocAdmin, request, queryset):
        return redirect('/index')

    HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
    changelist_actions = ('HomePage',)


# @admin.register(Jewel_media)
# class mediaJ(admin.ModelAdmin):
#     pass

# @admin.register(Blog)
# class blogadmin(admin.ModelAdmin):
#     pass

# @admin.register(Salesreturn_cs)
# class slreturncsadmin(ImportExportModelAdmin):
#     pass
