from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "covidus_main/home.html")


def enter(request):
    request_user = request._post['username']
    context = {
        "user": request_user
    }
    return render(request, "covidus_main/enter.html", context=context)
