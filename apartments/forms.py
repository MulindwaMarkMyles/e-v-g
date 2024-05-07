from django import forms
from .models import House
        
class AddHouse(forms.ModelForm):
    bedrooms = forms.IntegerField()
    floor = forms.IntegerField()
    price = forms.IntegerField()
    booked = forms.BooleanField()
    taken = forms.BooleanField()
    
    class Meta:
        model = House
        fields = ['bedrooms', 'floor', 'price', 'booked', 'taken']
        
    