from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns =[
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
    path('genhome/', views.genHome, name='genHome'),
    path('terms_and_conditions_2/', views.genChoice, name='tc_generator'),
    path('terms_and_conditions_questions/', views.termsform, name='termsform'),
    path('preview/', views.generate_terms, name='generate_terms'),
    path('view_saved_terms/<str:slug>',views.view_saved_terms, name='display_terms'),
    path('download/<str:company_name>/', views.download_pdf, name='download'),
    path('done/', views.done, name='done'),
    path('format/<str:company_name>/', views.format, name='format'),
    path('download/', views.download_page, name='download_option'),
    path('complete/', views.complete, name='complete'),
]