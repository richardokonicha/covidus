from django.urls import path
from covidus_main import views

urlpatterns = [
    path('', views.home, name='home')
]
