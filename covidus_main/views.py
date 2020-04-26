from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request, "covidus_main/home.html")


def enter(request):
    # request_user = request._post['username']
    # try:
    #     user = Profile.objects.get(username=request_user)
    # except DoesNotExist as e:
    #     pass
    context = {
        "user": "kjkj"
    }
    return render(request, "covidus_main/enter.html", context=context)



def get_data(request, *args, **kwargs):
    '''pass data to the chart'''
    value_list = list(value.values())
    lables_list = list(value.keys())
    data = {
        "value": value_list,
        "labels": lables_list, 
    }
    return JsonResponse(data) # http response


    

def pie_chart(request):
    labels = ['abj', 'kd', 'jos']
    data = [2, 6, 9]

    # queryset = City.objects.order_by('-population')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    return render(request, 'covidus_main/pie-chart.html', {
        'labels': labels,
        'data': data,
    })