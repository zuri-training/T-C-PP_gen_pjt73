from django.urls import path
from . import views

app_name = 'tc_gen'

urlpatterns =[
    path('tc-preview/', views.tc_preview, name='tc-preview'),
    path('tc-download/', views.tc_download, name='tc-download'),
<<<<<<< HEAD

    #adding routes for view functions of terms generator(jude)
=======
    path('genhome/', views.genHome, name='genHome'),
    path('terms and conditions 2/', views.genChoice, name='tc_generator'),
    path('terms and conditions questions/', views.termsform, name='termsform'),
    path('preview/', views.generate_terms, name='generate_terms'),
    path('view-saved-terms/<str:slug>',views.view_saved_terms, name='display_terms'),
    path('download/<str:company_name>/', views.download_pdf, name='download'),
    path('done/', views.done, name='done'),
    path('format/', views.format, name='format'),
    path('download/', views.download_page, name='download_option' ),
    path('complete/', views.complete, name='complete'),
>>>>>>> be123dc89c7107169d09d48fe2788180e92bbed0
]