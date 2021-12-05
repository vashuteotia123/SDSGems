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



@admin.register(clonePurchaseOfColorStones)
class ColorPurchaseOfColorStonesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in clonePurchaseOfColorStones._meta.fields]


if deploy_color_stone:
    
    @admin.register(countries)
    class CountryAdmin(ImportExportModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(color_of_colorstone)
    class ColorOfColorstoneAdmin(ImportExportModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(Treatment_cs)
    class treatcsadmin(ImportExportModelAdmin):
        # def HomePage(treatcsadmin, request, queryset):
        #         return redirect('/index')

        # HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
        # changelist_actions = ('HomePage',)
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

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

        HomePage.attrs = {'class': 'btn btn--success float-right', }
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
    class salesofcsadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(salesofcsadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right',}
        changelist_actions = ('HomePage',)

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



#Jewellery models here
if deploy_jewellery:
    @admin.register(jewell)
    class jewelladmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(centerstone)
    class CSadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(colorofcstone)
    class COCSadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(metal1)
    class metaladmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(shape1)
    class shapeadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    @admin.register(certificate)
    class certadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(certadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    # @admin.register(currencies)
    # class curradmin(DjangoObjectActions, admin.ModelAdmin):
    #     def HomePage(LocAdmin, request, queryset):
        # return redirect('/index')

    # HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
    # changelist_actions = ('HomePage',)

    @admin.register(Salesofjewellery)
    class salesofjewadmin(DjangoObjectActions, admin.ModelAdmin):
        search_fields = ['company_name']

        list_editable = ['company_name', ]
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

    @admin.register(Jewel_media)
    class mediaJ(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

if deploy_diamond:
    @admin.register(Diamond_media)
    class diamondMediaAdmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(shape_d)
    class shapedadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(clarity)
    class clarityadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(color_origin)
    class color_originadmin(ImportExportModelAdmin, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(white_color_grade)
    class white_color_gradeadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(fancy_color_intensity)
    class fancy_color_intensityadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(fancycolor_grade)
    class fancycolor_gradeadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(fluorescence_intensity)
    class fluoroscence_intensityadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(fluorescence_color)
    class fluorescence_intensityadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(certificate_d)
    class certificate_dadmin(ImportExportModelAdmin,admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(Salesofdiamond)
    class salesofdiaadmin(DjangoObjectActions, admin.ModelAdmin):
        search_fields = [f.name for f in Salesofdiamond._meta.fields]
        list_editable = ['date','company_name', 'price', 'amount_d', 'DIS_d', 'DIS_Amount_d', 'total_value_d', 'currency', 'tag_price_d', 'rate_d', 'salesapprovalstatus_d', 'comment']
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
    class PurchaseOFJewell(DjangoObjectActions, admin.ModelAdmin):
        list_editable = ['company_name']
        list_display = [f.name for f in POJ._meta.fields]
        readonly_fields = ['total', 'discount_amount']

    @admin.register(Inventoryofjewellery)
    class iojadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    

    

    

   

    @admin.register(PurchaseOfColorStones)
    class pcosadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

  

   

    

  

    @admin.register(Inventoryofcolorstones)
    class inventoryofcsadmin(ImportExportModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    

    @admin.register(POD)
    class PODadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(Inventoryofdiamond)
    class inventoryofdiamondadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)

    @admin.register(gemtype)
    class gemtypeadmin(ImportExportModelAdmin):
        def HomePage(gemtypeadmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    @admin.register(cut)
    class cutadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    @admin.register(polish)
    class polishadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    @admin.register(symmetry)
    class symmetryadmin(DjangoObjectActions, admin.ModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    @admin.register(location)
    class LocAdmin(ImportExportModelAdmin):
        def HomePage(LocAdmin, request, queryset):
            return redirect('/index')

        HomePage.attrs = {'class': 'btn btn-outline-success float-right', }
        changelist_actions = ('HomePage',)


    

   

   

    @admin.register(cloneInvofjewellery)
    class cloneInvofjewadmin(DjangoObjectActions, admin.ModelAdmin):
        list_display = [
            entry.name for entry in cloneInvofjewellery._meta.fields]
        list_editable = ["tag_price", "rate"]

    @admin.register(cloneInvofcolorstones)
    class cloneInvofcsadmin(DjangoObjectActions, admin.ModelAdmin):
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
    class cloneInvofdadmin(DjangoObjectActions, admin.ModelAdmin):
        list_display = [entry.name for entry in cloneInvofdiamond._meta.fields]
        list_editable = ["tag_price_d", "rate_d"]

    

    # @admin.register(ColorStone_media)
    # class ColorStone_media_admin(DjangoObjectActions, admin.ModelAdmin):
    #     list_display = [entry.name for entry in ColorStone_media._meta.fields]

    #     def response_change(self, request, obj=None):
    #         messages.success(request, "Media successfully changed!")
    #         return redirect('/index')

    #     def response_add(self, request, obj=None):
    #         messages.success(request, "Media successfully added!")
    #         return redirect('/index')

 








