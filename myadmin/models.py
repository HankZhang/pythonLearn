# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Good(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    goodName = models.CharField(max_length=20)
    goodPrice = models.FloatField(max_length=30)
    goodDesc = models.CharField(max_length=50)
    goodThumb = models.URLField(max_length=50)