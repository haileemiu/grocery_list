# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.db import models

class Category(models.Model):
  name =  models.CharField(max_length=100)
  
  class Meta:
      verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

class Item(models.Model):
  item = models.CharField(max_length=32)
  category =  models.ForeignKey(Category, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.item

  def get_absolute_url(self):
    return reverse('grocery_list:list')