from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import RegisterView, ContactLawyerView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name= 'signup'),
    path('signin/', views.login_view, name = 'signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('forgotPassword/', views.forgot, name='forgot'),
    path('contact_dashboard/', ContactLawyerView.as_view() , name='contact_dashboard'),
    path('history/', views.history, name='history'),
    path('logout/', views.logout, name='logout')
]
