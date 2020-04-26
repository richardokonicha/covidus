from django.shortcuts import render
from .models import Profile

# Create your views here.


def home(request):
    return render(request, "covidus_main/home.html")


def enter(request):
    request_user = request._post['username']
    try:
        user = Profile.objects.get(username=request_user)
    except covidus_main.models.Profile.DoesNotExist as e:
        pass
    context = {
        "user": request_user
    }
    return render(request, "covidus_main/enter.html", context=context)

