from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    bedrooms = models.IntegerField()
    floor = models.IntegerField()
    price = models.IntegerField()
    booked = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)
    type = models.CharField(max_length=100, null=True, blank=True)
    tag = models.SmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"House of id={self.id} and costs {self.price}."
    
    def save(self):
        super().save()
        return self.id

class Image(models.Model):
    image = models.ImageField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.image.url}"
        
class Meetings(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    house = models.CharField(max_length=100)
    remarks = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_scheduled = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return str(self.fullname + " for " + self.house)
    
class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} with email {self.email}"
    
    