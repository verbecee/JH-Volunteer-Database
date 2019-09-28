
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('application', views.vol_application, name='application'),
    path('apply', views.vol_start, name='start'),
    path('ideas', views.ideas, name='ideas'),

    # path('apply', views.create_application, name='createapplication'),
]
