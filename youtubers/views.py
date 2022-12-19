from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from .models import Youtuber

# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.all()
    data = {
        'tuber' : tubers
    }
    return render (request , 'youtubers\youtubers.html' , data)

def youtuber_details(request , id):
    tuber = get_object_or_404(Youtuber , pk = id)

    data =  {
        'tuber' : tuber
    } 
    return render (request , 'youtubers\youtuber_details.html' , data)


def search(request):
    tuber = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city' , flat = True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type' , flat = True).distinct()
    category_search = Youtuber.objects.values_list('category' , flat = True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tuber = tuber.filter(description__icontains = keyword)

    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tuber = tuber.filter(camera_type__iexact = camera)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tuber = tuber.filter(city__iexact = city)
   
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tuber = tuber.filter(category__iexact = category)


    data = {
        'tuber' : tuber,
        'city_search' : city_search,
        'camera_search' : camera_search,
        'category_search' : category_search,
    }
    return render (request , 'youtubers\search.html' , data)
