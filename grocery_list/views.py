# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import CreateView, ListView
from . import models

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ItemCreate(CreateView):
  model = models.Item
  fields = ['item', 'quantity', 'category']  

class GroceryListView(ListView):
  model = models.Item
  # context_object_name = 'grocery_list'
  paginate_by = 100

  def get_organized_data(self):

    items = models.Item.objects.all()
    categories = models.Category.objects.all()

    organized = {}

    for category in categories:
      assert isinstance(category, models.Category)
      items = list()

      organized_list = {
        'category': category,
        'item_list': items,
      }

      organized[category] = organized_list

      specific_items = models.Item.objects.select_related('category').filter(category_id=category.id)

      for item in specific_items:
        category = specific_items.category
        organized = organized[category]
        item_list=organized['items']
        items.append(item)

      return organized.items()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['grocery_list'] = self.get_organized_data()

    # context['list'] = models.Item.objects.select_related('category')
    return context