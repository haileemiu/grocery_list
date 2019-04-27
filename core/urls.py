from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('grocery_list/', include('grocery_list.urls')),
    path('admin/', admin.site.urls),
]
