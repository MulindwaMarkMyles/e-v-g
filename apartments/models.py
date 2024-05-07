from typing import Iterable
from django.db import models


class House(models.Model):
    bedrooms = models.IntegerField()
    floor = models.IntegerField()
    price = models.IntegerField()
    booked = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)
    
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