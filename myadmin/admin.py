# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myadmin.models import *


# Register your models here.
class MyAdmin(admin.AdminSite):
    site_header = "管理后台"
    site_title = "管理"

admin_site = MyAdmin(name="management")


class GoodAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'good_price', 'good_purchase_price', 'good_thumb')

admin_site.register(Good,GoodAdmin)
