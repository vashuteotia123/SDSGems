from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Database)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(countries)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(companyinfo)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(gemtype)
class gemtype(admin.ModelAdmin):
    pass 
@admin.register(POJ)
class PurchaseOFJewell(admin.ModelAdmin):
    pass

@admin.register(loc)
class LocAdmin(admin.ModelAdmin):
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
class curradm(admin.ModelAdmin):
    pass
# @admin.register(PurchaseOfColorStones)
# class pocsadmin(admin.ModelAdmin):
#     pass


@admin.register(Inventory)
class inventoryadm(admin.ModelAdmin):
    pass
@admin.register(shape1)
class shapeadm(admin.ModelAdmin):
    pass 