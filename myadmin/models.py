# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Good(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True,verbose_name="ID",name="id",editable=False)
    goodName = models.CharField(max_length=20,verbose_name="商品名",name="good_name")
    goodPrice = models.FloatField(max_length=30,verbose_name="售价",name="good_price")
    goodPurchasePrice = models.FloatField(max_length=1000,verbose_name="进货价",name="good_purchase_price")
    goodThumb = models.URLField(max_length=50,verbose_name="图片",name="good_thumb")

    class Meta:
        verbose_name_plural="商品"
        app_label = 'myadmin'  # 定义该model的app_label
        db_table = 'b_good_t'

