# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
from django.views.generic import CreateView, ListView
from . import models


def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")


class ItemCreate(CreateView):
  model = models.Item
  fields = ['item', 'category']  


class GroceryListView(ListView):
  model = models.Item
  # context_object_name = 'grocery_list'
  paginate_by = 100

  def get_organized_data(self):

    grocery_list = models.Item.objects.select_related('category')
    items_by_category = {}

    for item in grocery_list:
      if item.category.name not in items_by_category:
        items_by_category[item.category.name] = []

      items = items_by_category[item.category.name].append(item.item)
    
    return items_by_category.items()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['grocery_list'] = self.get_organized_data()
    return context

