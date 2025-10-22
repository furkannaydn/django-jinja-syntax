from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request,"template_app/first.html" )

def weather(request):
    weather_dictonary = {
        "city":"Istanbul",
        "temperature":30,
        "condition":"Sunny",
        "paris":[5,12,65,34],
        "rome":{"morning":22,"noon":28,"night":18},
        "user_premium":True,
    }
    return render(request,"template_app/weather.html", context=weather_dictonary)