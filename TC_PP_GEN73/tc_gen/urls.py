from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns = [
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
    path('terms and conditions/', views.tc_gen, name='tc_gen'),
    path('privacy policy/', views.privacy, name='privacy'),
    path('privacy policy 1/', views.privacy2, name='privacy2'),
    path('ready/', views.done, name='done'),
    path('format/', views.format, name='format'),
    path('complete/', views.complete, name='complete'),
    path('terms and conditions 2/', views.tc_gen2, name='tc_generator'),
    path('terms and conditions questions/', views.questions, name='questions'),
]