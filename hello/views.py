import requests
import subprocess
import os
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def jar(request):
    print('hit the jar endpoint')
    print(os.getcwd())
    subprocess.run('java -jar /app/java/barnacle-1.0-SNAPSHOT-jar-with-dependencies.jar', shell=True)
    return HttpResponse('<pre>' + 'hello world' + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

