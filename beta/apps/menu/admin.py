from django.contrib import admin

from apps.menu.models import Menu
from apps.menu.models import FoodItem


admin.site.register(FoodItem)
admin.site.register(Menu)
