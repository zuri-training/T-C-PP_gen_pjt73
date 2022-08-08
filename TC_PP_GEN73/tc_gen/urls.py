from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns = [
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
    path('terms and conditions/', views.tc_gen, name='tc_gen'),
    path('terms and conditions 2/', views.tc_gen2, name='tc_generator'),
    path('terms and conditions questions/', views.questions, name='questions'),
]