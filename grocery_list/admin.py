# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  pass