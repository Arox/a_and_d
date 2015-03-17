# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import MyUser
# Register your models here.

class ManagerMyUser(admin.ModelAdmin):
    pass

admin.site.register(MyUser, UserAdmin)