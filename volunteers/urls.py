
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vol_application, name='volunteer_apply1'),
]
