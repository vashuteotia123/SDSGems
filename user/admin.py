from django.contrib import admin
from django.contrib import messages
from import_export.admin import ImportExportModelAdmin

from django.shortcuts import redirect
from django_object_actions import DjangoObjectActions


# Register your models here.
from .models import *


@admin.register(User_table)
class User(ImportExportModelAdmin):
    search_fields = ['first_name', 'last_name', 'email_id', 'Businesstype']


@admin.register(countries)
class CountryAdmin(ImportExportModelAdmin):
    search_fields = ['country']


@admin.register(Blog)
class blogadmin(admin.ModelAdmin):

    search_fields = ['title', 'subject']


@admin.register(Subscribed_users)
class SubscribedAdmin(ImportExportModelAdmin):
    search_fields = ['email']


@admin.register(ConversionRate)
class ConversionAdmin(admin.ModelAdmin):
    pass


@admin.register(BirthStones)
class BirthStoneAdmin(admin.ModelAdmin):
    search_fields = ['name', 'month']
