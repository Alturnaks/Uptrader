from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    context.update({'menu_items': menu_items, 'menu_name': menu_name})
    return ''