# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myadmin.models import *


# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'good_price', 'good_purchase_price', 'good_thumb')

admin.site.register(Good,GoodAdmin)
