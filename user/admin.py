from django.contrib import admin
from django.contrib import messages
from import_export.admin import ImportExportModelAdmin

from django.shortcuts import redirect
from django_object_actions import DjangoObjectActions


# Register your models here.
from .models import *

@admin.register(User_table)
class User(admin.ModelAdmin):
    pass


@admin.register(countries)
class CountryAdmin(ImportExportModelAdmin):
    pass

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class blogadmin(DjangoObjectActions, admin.ModelAdmin):

    search_fields = ['title', 'subject']
    def response_change(self, request, obj):
        messages.success(request, "Blog changed successfully!")
        return redirect('/index')

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(request, "Blog added successfully!")
        return redirect('/index')