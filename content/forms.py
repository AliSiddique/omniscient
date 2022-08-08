from django.forms import ModelForm
from django import forms
from .models import Comment, Contact




class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        labels={"description":"Comment"}
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'What did you think of the article?'}),
        }



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name',"email","message"]
