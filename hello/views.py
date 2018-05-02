from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import os

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    # return HttpResponse('Hello! ' * times)
    return HttpResponse('Hello from Python!')


