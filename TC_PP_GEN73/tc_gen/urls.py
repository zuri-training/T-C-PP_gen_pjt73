from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns = [
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),

    #adding routes for view functions of terms generator(jude)
    path('', views.termsform, name='home'),
    path('/generator', views.generate_terms, name='terms'),
    path('/view-saved-terms/<str:slug>', views.view_saved_terms, name='display_terms'),
    path('/download/<str:company_name>', views.download_pdf, name='download'),
]