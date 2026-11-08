from django.urls import path
from rest_framework.routers import DefaultRouter as router

from .views import MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('menu/items', MenuItemView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/tables', BookingView.as_view({
        'get': 'list',
        'post': 'create',
    }))
]
