from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemAdmin

admin.site.register(MenuItem, MenuItemAdmin)