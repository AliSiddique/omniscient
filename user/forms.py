from django.forms import ModelForm
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm  
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username","name","email","password1","password2",]


class WriterForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['name','email','uni','bio','image','phone','twitter','website','slug']  


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['name','email']                    