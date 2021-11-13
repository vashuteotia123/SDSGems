from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
# Register your models here.

development_mode = True

if development_mode:
    @admin.register(Database)
    class DataAdmin(admin.ModelAdmin):
        pass

    @admin.register(countries)
    class CountryAdmin(admin.ModelAdmin):
        pass

    @admin.register(companyinfo)
    class CompanyAdmin(admin.ModelAdmin):
        actions = ['change_name']
        search_fields = ['company_name']
        list_display = [f.name for f in companyinfo._meta.fields]

        def change_name(self, request, queryset):
            queryset.update(company_name="tanishq")

    @admin.register(POJ)
    class PurchaseOFJewell(admin.ModelAdmin):
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
    class certadmin(admin.ModelAdmin):
        pass

    @admin.register(currencies)
    class curradmin(admin.ModelAdmin):
        pass

    @admin.register(PurchaseOfColorStones)
    class pcosadmin(admin.ModelAdmin):
        pass


    @admin.register(Treatment_cs)
    class treatcsadmin(admin.ModelAdmin):
        pass

    @admin.register(Origin_cs)
    class originadmin(admin.ModelAdmin):
        pass

    @admin.register(cert_no_cs)
    class certadmin(admin.ModelAdmin):
        pass

    @admin.register(Lab_cs)
    class labadmin(admin.ModelAdmin):
        pass

    @admin.register(shape_cs)
    class shapeadmin(admin.ModelAdmin):
        pass

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
        list_display = [f.name for f in Salesofjewellery._meta.fields]

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

    @admin.register(Salesofcolorstones)
    class salesofcsadmin(admin.ModelAdmin):
        pass

    @admin.register(cloneInvofdiamond)
    class cloneInvofdadmin(admin.ModelAdmin):
        list_display = [entry.name for entry in cloneInvofdiamond._meta.fields]
        list_editable = ["tag_price_d", "rate_d"]

    @admin.register(Salesofdiamond)
    class salesofdadmin(admin.ModelAdmin):
        pass

    # @admin.register(Salesreturn)
    # class salesofdadmin(admin.ModelAdmin):
    #     pass


@admin.register(gemtype)
class gemtypeadmin(admin.ModelAdmin):
    pass


@admin.register(cut)
class cutadmin(admin.ModelAdmin):
    pass


@admin.register(polish)
class polishadmin(admin.ModelAdmin):
    pass


@admin.register(symmetry)
class symmetryadmin(admin.ModelAdmin):
    pass


@admin.register(location)
class LocAdmin(admin.ModelAdmin):
    pass


@admin.register(Jewel_media)
class mediaJ(admin.ModelAdmin):
    pass

@admin.register(Blog)
class blogadmin(admin.ModelAdmin):
    pass

@admin.register(Salesreturn_cs)
class slreturncsadmin(admin.ModelAdmin):
    pass