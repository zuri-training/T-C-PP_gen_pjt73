from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='index'),
    path('/service',views.service,name='service'),

]
