from django.shortcuts import render
import requests
from django.utils import timezone

# Create your views here.
def index(request):

    data = True
    global_summary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            global_summary = result.json()['Global']
            countries = result.json()['Countries']
            data = False
        except:
            data = True
    return render(request, 'home.html', {'result': result, 'global_summary':global_summary, 'countries':countries})


def india(request):

    url2 = ('https://api.covidindiatracker.com/total.json')
    res2 = requests.get(url2).json()

    url = ('https://api.covidindiatracker.com/state_data.json')
    res = requests.get(url).json()

    return render(request, 'india.html', {'res': res, 'res2':res2})


