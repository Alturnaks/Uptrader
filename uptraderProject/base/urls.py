from django.urls import path
from .views import draw_menu

urlpatterns = [
    path('menu/', draw_menu.as_view(), name='menu_view'),
]
