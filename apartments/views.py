from django.shortcuts import redirect, render
from .models import *
from random import randint
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import faker

fake = faker.Faker()

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
        "title":"SK-GRACE APARTMENTS",
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
        "title":"SK-GRACE APARTMENTS",
        "houses":houses_and_images,
        "page":"Properties"
    }
    
    return render(request, "properties.html", context)

def details(request, id):
    house = House.objects.filter(id=id).first()
    images = house.image_set.all()
    context = {
        "title":"SK-GRACE APARTMENTS",
        "page":"details",
        "house":house,
        "images":images,
        "image_count": range(images.count())
    }
    return render(request, "property-details.html", context)

def contacts(request):
    context = {
        "title":"SK-GRACE APARTMENTS",
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
        "title":"SK-GRACE APARTMENTS",
        "form": form,
        
    }
    return render(request, "upload.html", context)

def site_map(request):
    context = {
        "title": "SK-GRACE APARTMENTS"
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
        "title": "SK-GRACE APARTMENTS",
        "form":form
    }
    return render(request, "schedule.html", context)
    
@login_required(login_url="/sk-grace/admin/login/")
def admin(request):
    houses = House.objects.all()
    house_and_image = []
    users = User.objects.all()
    for house in houses:
        house_and_image.append((house, house.image_set.all()[randint(0,(len(house.image_set.all()) -1))]))
    context = {
        "house_and_image": house_and_image,
        "users": users
    }
    return render(request, "admin.html", context)

def login_u(request):
    if request.method ==  "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).first().username
            print(username, password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("administrator")
            return render(request, "login.html", {"error":"Invalid email or password"})
        else:
            return render(request, "login.html", {"error":"Invalid email or password"})
        
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = REGISTERADMIN(request.POST)
        if form.is_valid():
            form.save()
            random_username = fake.user_name()
            while User.objects.filter(username=random_username).exists():
                random_username = fake.user_name()
                
            user = User.objects.create_superuser(username=random_username, email=form.cleaned_data.get("email"), password=form.cleaned_data.get("password1"), first_name=form.cleaned_data.get("name").split(" ")[0], last_name=form.cleaned_data.get("name").split(" ")[1])
            
            if user:
                admin = Admin.objects.filter(name=form.cleaned_data.get("name")).first()
                admin.user = user
                admin.save()
                login(request, user)
                return redirect("administrator")
        else:
            print("Form is not valid: ", form.errors)
            return render(request, "register.html", {"form":form})
    form = REGISTERADMIN()
     
    context = {
        "form": form
    }
    return render(request, "register.html", context)
    
def logout_u(request):
    logout(request)
    return redirect("home")