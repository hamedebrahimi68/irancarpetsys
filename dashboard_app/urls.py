from django.urls import path
from .views import dashboard_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),

    
    # convenience routes used by the template — map to dashboard_view as placeholders
    path('profile/', dashboard_view, name='profile'),
    path('mail/', dashboard_view, name='mail'),
    path('file-manager/', dashboard_view, name='file_manager'),
    path('mail-settings/', dashboard_view, name='mail_settings'),
    path('chat/', dashboard_view, name='chat'),
    path('cart/', dashboard_view, name='cart'),
    path('logout/', dashboard_view, name='logout'),
]