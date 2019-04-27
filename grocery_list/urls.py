from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.GroceryListView.as_view(), name='list'),
    path('new/', views.ItemCreate.as_view(), name='new-item'),

]