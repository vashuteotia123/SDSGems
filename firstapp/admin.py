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
    actions=['return']
    search_fields = ['company_name']
    list_display=[f.name for f in companyinfo._meta.fields]

@admin.register(gemtype)
class gemtype(admin.ModelAdmin):
    pass 
@admin.register(POJ)
class PurchaseOFJewell(admin.ModelAdmin):
    pass
@admin.register(Inventoryofjewellery)
class iojadmin(admin.ModelAdmin):
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
@admin.register(PurchaseOfColorStones)
class pocsadmin(admin.ModelAdmin):
    pass
    
@admin.register(Treatment_cs)
class treatcsadmin(admin.ModelAdmin):
    pass
@admin.register(Origin_cs)
class originadmin(admin.ModelAdmin):
    pass
@admin.register(certificate_no_cs)
class certadmin(admin.ModelAdmin):
    pass
@admin.register(Lab_cs)
class labadmin(admin.ModelAdmin):
    pass
@admin.register(shape_cs)
class shapeadmin(admin.ModelAdmin):
    pass
@admin.register(Inventoryofcolorstones)
class inventoryofcsadm(admin.ModelAdmin):
    pass
@admin.register(shape1)
class shapeadm(admin.ModelAdmin):
    pass 
