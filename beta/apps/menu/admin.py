from django.contrib import admin

from apps.menu.models import Menu
from apps.menu.models import FoodItem
from apps.menu.models import Category

admin.site.register(FoodItem)
admin.site.register(Menu)
admin.site.register(Category)