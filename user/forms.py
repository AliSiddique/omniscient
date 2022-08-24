from django.forms import ModelForm
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError
from django import forms
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields=["username","name","email","password1","password2"]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None
            
class WriterForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['username','name','email','uni','bio','image','phone','twitter','website','slug']
        labels ={"slug":"URL <small>(Your name in the URL)</small>","image":"Profile image","uni":"University"}

        def clean_email(self):
            data = self.cleaned_data["URL"]
            if data == " ":
                raise ValidationError("You must have a URL at all times")

            return data    
  


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['name','email']                
        


class CancelSubscription(forms.Form):
    hidden = forms.HiddenInput()