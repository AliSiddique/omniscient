from django.forms import ModelForm
from .models import User

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields=["username","name","email","password"]