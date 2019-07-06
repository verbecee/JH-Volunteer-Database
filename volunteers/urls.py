
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apply', views.vol_application, name='volunteer'),
    # path('apply', views.create_application, name='createapplication'),
]
