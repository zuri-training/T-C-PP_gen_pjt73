from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login_page.html'), name = 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('contact_dashboard/', views.contact, name='contact_dashboard'),
    path('history/', views.history, name='history'),

    path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logout_page.html'), name = 'logout'),
]
