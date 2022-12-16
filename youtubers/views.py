from django.shortcuts import render
from .models import Youtuber

# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.all()
    data = {
        'tuber' : tubers
    }
    return render (request , 'youtubers\youtubers.html' , data)

def youtuber_details(request , id):
    return render (request , 'youtubers\youtuber_details.html')


def search(request):
    pass
