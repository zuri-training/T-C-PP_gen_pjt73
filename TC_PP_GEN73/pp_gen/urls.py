from django.urls import path
from . import views

app_name = 'pp_gen'

urlpatterns = [
    path('privacy/', views.privacy, name='privacy'),
]
