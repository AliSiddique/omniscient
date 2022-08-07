from django.forms import ModelForm
from .models import Comment, Contact




class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        labels={"description":"What are your thoughts?"}



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name',"email","message"]
