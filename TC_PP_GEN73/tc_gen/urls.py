from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns = [
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
    path('genhome/', views.genHome, name='genHome'),
    path('terms and conditions 2/', views.genChoice, name='tc_generator'),
    path('terms and conditions questions/', views.termsform, name='termsform'),
    path('addinfo/', views.tc_addinfo, name='addinfo'),
    path('preview/', views.generate_terms, name='generate_terms'),
    path('view-saved-terms/<str:slug>',views.view_saved_terms, name='display_terms'),
    path('download/<str:company_name>', views.download_pdf, name='download'),
    path('terms and conditions/', views.tc_gen, name='tc_gen'),
    path('privacy policy/', views.privacy, name='privacy'),
    path('privacy policy 1/', views.privacy2, name='privacy2'),
    path('ready/', views.done, name='done'),
    path('format/', views.format, name='format'),
    path('complete/', views.complete, name='complete'),
    path('terms and conditions 2/', views.tc_gen2, name='tc_generator'),
    path('terms and conditions questions/', views.questions, name='questions'),
]

#>>>>>>> f047f7c62e7dbea252034d06829c6fe8a561f1db
