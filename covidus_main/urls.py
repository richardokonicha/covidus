from django.urls import path
from covidus_main import views

app_name = "covidus_main"
urlpatterns = [
    path('', views.home, name='home'),
    path("enter", views.enter, name="enter")
]
