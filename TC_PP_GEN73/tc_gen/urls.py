from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns = [
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
]