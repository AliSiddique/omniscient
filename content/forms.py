from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Comment, Contact,BecomeWriter




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


class BecomeWriterForm(ModelForm):
    class Meta:
        model = BecomeWriter
        fields = ['name','email','year','univeristy','course','field','file']
        labels={"year":"What year are you in?","univeristy":"University","course":"What do you study?","file":"CV/Cover letter","field":"What subject do you want to write for?  <small>(you can change this later)</small>"}
      
        def clean_email(self):
            data = self.cleaned_data["email"]
            if ".ac.uk" not in data:
                raise ValidationError("You must have a univeristy email to sign up")

            return data    
     
