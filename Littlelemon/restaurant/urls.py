from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('menu-items', MenuItemView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/tables', BookingView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('api-token-auth', obtain_auth_token),
]
