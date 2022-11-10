from django.urls import path
from . import views

urlpatterns = [
    path('', views.state, name='state'),
    path('', views.reset, name='reset'),
    path('cus', views.cus, name='cus'),
    path('stud', views.stud, name='stud'),
]