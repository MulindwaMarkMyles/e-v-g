from django import forms
from .models import House, Meetings, Admin
from django.core.exceptions import ValidationError
import uuid
        
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
        
        
class REGISTERADMIN(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    token = forms .UUIDField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    
    fields = ['name', 'email', 'password1', 'password2', 'token']
        
        
    def __init__(self, *args, **kwargs):
        super(REGISTERADMIN, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = "John Doe"
        self.fields['email'].widget.attrs['placeholder'] = "johndoe@gmail.com"
        self.fields['token'].widget.attrs['placeholder'] = "123f-323s-233d-236d-df43-asf2"
        self.fields['password1'].widget.attrs['placeholder'] = "johnde123"
        self.fields['password2'].widget.attrs['placeholder'] = "johnde123"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            
    def validate_password(self, password, name):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter."	)
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char in "!@#$%^&*()-_+=~`[]{}|:;\"'<>,.?/" for char in password):
            raise ValidationError("Password must contain at least one special character.")
        if Admin.objects.filter(name=name).exists():
            raise ValidationError("That administrator already exists.")
        name = name.split(" ")
        for n in name:
            if password.find(n.lower()) != -1:
                raise ValidationError("Password must not contain your name.")

            
    def clean(self):
        cleaned_data = super(REGISTERADMIN, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        name = cleaned_data.get("name")
        
        if password1 and password2:
            if password1 != password2:
                self.add_error("password2", "Passwords do not match")
            try:
                self.validate_password(password1, name)
            except ValidationError as e:
                self.add_error("password1", e.message)

        token = cleaned_data.get("token")
        
        if not Admin.objects.filter(token=token).exists():
            self.add_error("token", "Invalid token")

        return cleaned_data
            
    def save(self):
        admin = Admin(
            name=self.cleaned_data.get("name"),
            email=self.cleaned_data.get("email"),
            token=uuid.uuid4(),
        )
        
        admin.save()
        return admin
            
    