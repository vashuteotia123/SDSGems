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
deploy_jewellery = True
deploy_diamond = True


# @admin.register(clonePurchaseOfColorStones)
# class ColorPurchaseOfColorStonesAdmin(admin.ModelAdmin):
#     list_display = [f.name for f in clonePurchaseOfColorStones._meta.fields]


if deploy_color_stone:

    @admin.register(countries)
    class CountryAdmin(ImportExportModelAdmin):
        search_fields = [f.name for f in countries._meta.fields]

    @admin.register(color_of_colorstone)
    class ColorOfColorstoneAdmin(ImportExportModelAdmin):
        search_fields = [f.name for f in color_of_colorstone._meta.fields]

    @admin.register(Treatment_cs)
    class treatcsadmin(ImportExportModelAdmin):
        search_fields = [f.name for f in Treatment_cs._meta.fields]

    @admin.register(Origin_cs)
    class originadmin(ImportExportModelAdmin):
        search_fields = [f.name for f in Origin_cs._meta.fields]

    @admin.register(Lab_cs)
    class labadmin(ImportExportModelAdmin):
        search_fields = [f.name for f in Lab_cs._meta.fields]

    @admin.register(shape_cs)
    class shapeadmin(ImportExportModelAdmin):
        search_fields = [f.name for f in shape_cs._meta.fields]

    @admin.register(companyinfo)
    class CompanyAdmin(admin.ModelAdmin):
        search_fields = [f.name for f in companyinfo._meta.fields]
        list_display_links = [f.name for f in companyinfo._meta.fields]
        list_display = [f.name for f in companyinfo._meta.fields]

    @admin.register(ColorStone_media)
    class ColorStone_media_admin(admin.ModelAdmin):
        list_display = [entry.name for entry in ColorStone_media._meta.fields]
        search_fields = [f.name for f in ColorStone_media._meta.fields]

    @admin.register(Salesofcolorstones)
    class salesofcsadmin(admin.ModelAdmin):

        formfield_overrides = {models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 40})}, }
        search_fields = ['company_name__company_name', 'stockid',
                         'location__place', 'gem_type__gem', 'shape__shape', 'treatment__treatment']
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
        search_fields = [f.name for f in currencies._meta.fields]

    @admin.register(gemtype)
    class gemtypeadmin(ImportExportModelAdmin):
        search_fields_ = [f.name for f in gemtype._meta.fields]


# Jewellery models here
if deploy_jewellery:
    @admin.register(jewell)
    class jewelladmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in jewell._meta.fields]

    @admin.register(centerstone)
    class CSadmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in centerstone._meta.fields]

    @admin.register(colorofcstone)
    class COCSadmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in colorofcstone._meta.fields]

    @admin.register(metal1)
    class metaladmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in metal1._meta.fields]

    @admin.register(shape1)
    class shapeadmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in shape1._meta.fields]

    @admin.register(certificate)
    class certadmin(ImportExportModelAdmin, admin.ModelAdmin):
        search_fields = [f.name for f in certificate._meta.fields]

    # @admin.register(currencies)
    # class curradmin( admin.ModelAdmin):
    #     def HomePage(LocAdmin, request, queryset):
        # return redirect('/index')

    # HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
    # changelist_actions = ('HomePage',)

    @admin.register(Salesofjewellery)
    class salesofjewadmin(admin.ModelAdmin):
        formfield_overrides = {models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 40})}, }
        search_fields = ['company_name__company_name', 'stockid', 'jewellery_type__jewel',
                         'center_stone__stone', 'color_of_center_stone__color', 'shape__shape', 'metal__metal']

        list_editable = ['company_name', 'amount', 'currency', 'total_value',
                         'comment', 'tag_price', 'salesapprovalstatus', 'rate', 'DIS', 'DIS_amount']
        list_display = [f.name for f in Salesofjewellery._meta.fields]

        def has_add_permission(self, request, obj=None):
            return False

        def has_change_permission(self, request, obj=None):
            return True

        def has_delete_permission(self, request, obj=None):
            return False

        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(Jewel_media)
    class mediaJ(admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

if deploy_diamond:
    @ admin.register(Diamond_media)
    class diamondMediaAdmin(admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(shape_d)
    class shapedadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(clarity)
    class clarityadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(color_origin)
    class color_originadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(white_color_grade)
    class white_color_gradeadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    # @admin.register(fancy_color_intensity)
    # class fancy_color_intensityadmin(ImportExportModelAdmin,admin.ModelAdmin):
    #     def HomePage(LocAdmin, request, queryset):
    #         return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    # @admin.register(fancycolor_grade)
    # class fancycolor_gradeadmin(ImportExportModelAdmin,admin.ModelAdmin):
    #     def HomePage(LocAdmin, request, queryset):
    #         return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(fluorescence_intensity)
    class fluoroscence_intensityadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(fluorescence_color)
    class fluorescence_intensityadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(certificate_d)
    class certificate_dadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(Salesofdiamond)
    class salesofdiaadmin(admin.ModelAdmin):
        search_fields = ['company_name__company_name', 'stockid',
                         'location__place', 'shape__shape', 'clarity__clarity', 'color_origin1__c_o',
                         'white_color_grade1__w_c_g', 'fancycolor_grade', 'cut__cut', 'polish__polish', 'symmetry__symmetry', ]
        list_editable = ['date', 'company_name', 'price', 'amount_d', 'DIS_d', 'DIS_Amount_d',
                         'total_value_d', 'currency', 'tag_price_d', 'rate_d', 'salesapprovalstatus_d', 'comment']
        list_display = [f.name for f in Salesofdiamond._meta.fields]

        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

        def has_add_permission(self, request, obj=None):
            return False

        def has_change_permission(self, request, obj=None):
            return True

        def has_delete_permission(self, request, obj=None):
            return False

        @ admin.register(location)
        class LocAdmin(ImportExportModelAdmin):
            def HomePage(LocAdmin, request, queryset):
                return redirect('/index')

            HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
            changelist_actions = ('HomePage',)

        @ admin.register(cut)
        class cutadmin(admin.ModelAdmin):
            def HomePage(cutadmin, request, queryset):
                return redirect('/index')

            HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
            changelist_actions = ('HomePage',)

        @ admin.register(polish)
        class polishadmin(admin.ModelAdmin):
            def HomePage(polishadmin, request, queryset):
                return redirect('/index')

            HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
            changelist_actions = ('HomePage',)

        @ admin.register(symmetry)
        class symmetryadmin(admin.ModelAdmin):
            def HomePage(symmetryadmin, request, queryset):
                return redirect('/index')

            HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
            changelist_actions = ('HomePage',)


if development_mode:
    @ admin.register(POJ)
    class PurchaseOFJewell(admin.ModelAdmin):
        list_editable = ['company_name']
        list_display = [f.name for f in POJ._meta.fields]
        readonly_fields = ['total', 'discount_amount']

    @ admin.register(Inventoryofjewellery)
    class iojadmin(admin.ModelAdmin):
        def HomePage(iojadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(PurchaseOfColorStones)
    class pcosadmin(admin.ModelAdmin):
        def HomePage(pcosadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(Inventoryofcolorstones)
    class inventoryofcsadmin(ImportExportModelAdmin):
        def HomePage(inventoryofcsadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(POD)
    class PODadmin(admin.ModelAdmin):
        def HomePage(PODadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(Inventoryofdiamond)
    class inventoryofdiamondadmin(admin.ModelAdmin):
        def HomePage(inventoryofdiamondadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @ admin.register(cloneInvofjewellery)
    class cloneInvofjewadmin(admin.ModelAdmin):
        list_display = [
            entry.name for entry in cloneInvofjewellery._meta.fields]
        list_editable = ["tag_price", "rate"]

    @ admin.register(cloneInvofcolorstones)
    class cloneInvofcsadmin(admin.ModelAdmin):
        list_display = [
            entry.name for entry in cloneInvofcolorstones._meta.fields]
        list_editable = ["tag_price_cs", "rate_cs"]

    # @admin.register(Salesofcolorstones)
    # class salesofcsadmin(admin.ModelAdmin):
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

    @ admin.register(cloneInvofdiamond)
    class cloneInvofdadmin(admin.ModelAdmin):
        list_display = [entry.name for entry in cloneInvofdiamond._meta.fields]
        list_editable = ["tag_price_d", "rate_d"]

    # @admin.register(ColorStone_media)
    # class ColorStone_media_admin( admin.ModelAdmin):
    #     list_display = [entry.name for entry in ColorStone_media._meta.fields]

    #     def response_change(self, request, obj=None):
    #         messages.success(request, "Media successfully changed!")
    #         return redirect('/index')

    #     def response_add(self, request, obj=None):
    #         messages.success(request, "Media successfully added!")
    #         return redirect('/index')
