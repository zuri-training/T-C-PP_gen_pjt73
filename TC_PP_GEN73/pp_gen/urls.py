from django.urls import path
from . import views
# index, generate_policy, view_saved_policies, download_pdf
app_name = 'pp_gen'

urlpatterns = [
    path('privacy/', views.index, name='privacy'),
    path('preview/', views.generate_policy, name='generate_policy'),
    path('view_saved_policies/<str:slug>/', views.view_saved_policies, name='display_policies'),
    path('download/<str:company_name>/', views.download_pdf, name='download'),
    path('format/<str:company_name>/', views.format, name='format')
]
