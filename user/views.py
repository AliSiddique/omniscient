from multiprocessing import context
import profile
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.views import LoginView
from .forms import CreateUserForm,ProfileForm, WriterForm
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from .models import Profile, User
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
class UserSignupView(CreateView):
    template_name = "user/signup.html"
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('')


class LoginView(LoginView):
    template_name = "user/login.html"
            




def profiles(request):
    profiles = Profile.objects.filter(is_writer=True)
    context={
        "profiles":profiles
    }
    return render(request,"user/profiles.html",context)

def single_profile(request,slug):
    profile = Profile.objects.get(slug=slug)    
    content = profile.article_set.all()
   
    context={
        "profile":profile,
        "posts":content

    }     
    return render(request,"user/single-profile.html",context)
    

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "user/passwordchange.html"



def editAccount(request):
    profile = request.user.profile
    if request.user.profile.is_writer:
        form = WriterForm(instance=profile)
        if request.method == 'POST':
            form = WriterForm(request.POST,request.FILE,instance=profile)
            if form.is_valid():
                form.save()
            return redirect('profile')   


    else:
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILE,instance=profile)
            if form.is_valid():
                form.save()
            return redirect('profile')   
              
    context ={
        'form':form
    }
    return render(request,"user/settings.html",context)




def logout_view(request):
    logout(request)
    return redirect('article-list') 