from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'parent', 'url', 'is_active']
        widgets = {'parent': forms.Select(attrs={'class': 'select2'})}

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ['title', 'url', 'parent', 'is_active']
    list_filter = ['parent', 'is_active']
    search_fields = ['title', 'url']