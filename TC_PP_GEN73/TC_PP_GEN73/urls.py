"""TC_PP_GEN73 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('tc_gen/', include('tc_gen.urls')),
    path('social_auth/', include('social_django.urls'), name='social'),

    #password reset url
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),
    name = 'password_reset'),

    #password reset done url
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),
    name = 'password_reset_done'),

    #password reset confirm url
    path('password-reset/confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'),
    name = 'password_reset_confirm'),           

    #password reset complete url
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name = 'accounts/password_reset_complete.html'), name = 'password_reset_complete'),
]
