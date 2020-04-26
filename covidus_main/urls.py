from django.urls import path
from covidus_main import views
from django.conf.urls import url


app_name = "covidus_main"
urlpatterns = [
    path('', views.home, name='home'),
    path("enter", views.enter, name="enter"),
    url(r'^api/data/$', views.get_data, name='api-data'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]


