from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import os
#remember to start a new 'pipenv shell'
# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    # return HttpResponse('Hello! ' * times)
    return HttpResponse('Hello from Python!')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'index.html', {'greetings': greetings})

