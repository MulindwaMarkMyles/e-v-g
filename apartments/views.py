from django.shortcuts import redirect, render
from .models import *
from random import randint
from .forms import *

def home(request):
    random_house = House.objects.filter(id=6).first() # make this random after fixing all problems
    taken = "No" if not random_house.taken else "Yes"
    booked = "No" if not random_house.booked else "Yes"
    images = random_house.image_set.all()
    image = images[randint(0,(len(images) -1))]
    
    houses = House.objects.all()
    images = []
    
    for house in houses:
        images.append(house.image_set.all()[randint(0,(len(house.image_set.all()) -1))])
        
    houses_and_images = zip(houses, images)
    
    context = {
        "title":"EVERGRACE APARTMENTS",
        "page":"home",
        "house":random_house,
        "booked":booked,
        "taken":taken,
        "image": image,
        "houses":houses_and_images
    }
    return render(request, "index.html", context)

def properties(request):
    houses = House.objects.all()
    images = []
    
    for house in houses:
        images.append(house.image_set.all()[randint(0,(len(house.image_set.all()) -1))])
        
    houses_and_images = zip(houses, images)
    
    context = {
        "title":"EVERGRACE APARTMENTS",
        "houses":houses_and_images,
        "page":"Properties"
    }
    
    return render(request, "properties.html", context)

def details(request, id):
    house = House.objects.filter(id=id).first()
    images = house.image_set.all()
    context = {
        "title":"EVERGRACE APARTMENTS",
        "page":"details",
        "house":house,
        "images":images,
        "image_count": range(images.count())
    }
    return render(request, "property-details.html", context)

def contacts(request):
    context = {
        "title":"EVERGRACE APARTMENTS",
        "page":"contacts"
    }
    return render(request, "contact.html", context)

def upload(request):
    if request.method == "POST":
        form = AddHouse(request.POST)
        if form.is_valid():
            house_id = form.save().id
            images = request.FILES.getlist('images')
            house = House.objects.filter(id=house_id).first()
            for image in images:
                Image.objects.create(image=image, house=house)
            print('\n\n\n\n\nDONE EDITING\n\n\n')
    else:
        form = AddHouse()
    
    context = {
        "title":"EVERGRACE APARTMENTS",
        "form": form,
        
    }
    return render(request, "upload.html", context)

def site_map(request):
    context = {
        "title": "EVERGRACE APARTMENTS"
    }
    return render(request, "map.html", context)

def schedule(request):
    if request.method == 'POST':
        form = ScheduleMeeting(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.add_error(None, "Please check the details you entered.")
    else:
        form = ScheduleMeeting()
        
    context = {
        "title": "EVERGRACE APARTMENTS",
        "form":form
    }
    return render(request, "schedule.html", context)
    
def admin(request):
    properties = House.objects.all()
    context = {
        "properties": properties
    }
    return render(request, "admin.html", context)