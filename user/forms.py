from django.forms import ModelForm
from .models import User,Profile

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields=["username","name","email","password"]


class WriterForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['name','email','uni','bio','image','phone','twitter','website','slug']  


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['name','email']                    