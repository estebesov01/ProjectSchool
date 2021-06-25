from django.http import request
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def days(request):
    return render(request, 'main/days.html')