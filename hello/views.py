from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import os
#remember to start a new 'pipenv shell'
# Create your views here.
def index(request):
    return render(request, "index.html" )

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {'greetings': greetings})

def output(request):
    if request.is.ajax():
        py_obj = mrcode.test_code(10)
        return render( request, 'hello/output.html', {'output': py_obj.a } )

