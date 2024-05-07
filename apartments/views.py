from django.shortcuts import render
from .models import *
from random import randint
from .forms import *

def home(request):
    random_house = House.objects.filter(id=6).first() # make this random after fixing all problems
    taken = "No" if not random_house.taken else "Yes"
    booked = "No" if not random_house.booked else "Yes"
    images = random_house.image_set.all()
    image = images[randint(0,(len(images) -1))]
    print(image.image.url)
    context = {
        "title":"EVERGRACE APARTMENTS",
        "house":random_house,
        "booked":booked,
        "taken":taken,
        "image": image
    }
    return render(request, "index.html", context)

def properties(request):
    context = {
        "title":"EVERGRACE APARTMENTS"
    }
    return render(request, "properties.html", context)

def details(request):
    context = {
        "title":"EVERGRACE APARTMENTS"
    }
    return render(request, "property-details.html", context)

def contacts(request):
    context = {
        "title":"EVERGRACE APARTMENTS"
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
        

