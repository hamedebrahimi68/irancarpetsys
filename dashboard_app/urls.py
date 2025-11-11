from django.urls import path
from .views import dashboard_view, login_view, logout_view

urlpatterns = [
    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Dashboard and main views
    path('', dashboard_view, name='dashboard'),
    path('profile/', dashboard_view, name='profile'),
    path('mail/', dashboard_view, name='mail'),
    path('file-manager/', dashboard_view, name='file_manager'),
    path('mail-settings/', dashboard_view, name='mail_settings'),
    path('chat/', dashboard_view, name='chat'),
    path('cart/', dashboard_view, name='cart'),
]