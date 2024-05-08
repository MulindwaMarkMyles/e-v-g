from django import forms
from .models import House, Meetings
import datetime
        
class AddHouse(forms.ModelForm):
    bedrooms = forms.IntegerField()
    floor = forms.IntegerField()
    price = forms.IntegerField()
    booked = forms.BooleanField()
    taken = forms.BooleanField()
    
    class Meta:
        model = House
        fields = ['bedrooms', 'floor', 'price', 'booked', 'taken']
        
class ScheduleMeeting(forms.ModelForm):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    house = forms.CharField(required=True)
    remarks = forms.TextInput()
    date_scheduled = forms.DateTimeField(label="Date and Time",
                                        required=True,
                                        widget=forms.DateTimeInput(attrs={"class":"datepicker", "type":"datetime-local"}),
                            )
    
    class Meta:
        model = Meetings
        fields = ['fullname', 'email', 'house', 'remarks', 'date_scheduled']
        
    def __init__(self, *args, **kwargs):
        super(ScheduleMeeting, self).__init__(*args, **kwargs)
        
        self.fields['fullname'].widget.attrs['placeholder'] = "Example: John Doe"
        self.fields['email'].widget.attrs['placeholder'] = "Example: johndoe@email.com"
        self.fields['house'].widget.attrs['placeholder'] = "Example: 2 Bedrooms"
        self.fields['remarks'].widget.attrs['placeholder'] = "Example: Visit, tour, love these apartments ....."
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'meeting-form-field'
            self.fields[field_name].help_text = ''
        
    