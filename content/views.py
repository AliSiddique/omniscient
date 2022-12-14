from cmath import log
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,reverse
from django.views.generic import DetailView,CreateView
from django.utils import timezone
from content.forms import BecomeWriterForm, CommentForm, ContactForm
from django.views.generic.edit import FormMixin
from django.contrib import messages
from content.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
import logging
# Create your views here.
def ArticleList(request):  
    economy = Article.objects.filter(category='Ec').filter(published=True)[:7]
    finance = Article.objects.filter(category='FI').filter(published=True)[:7]
    politics = Article.objects.filter(category='Po').filter(published=True)[:4]

    context={
        "Economy":economy,
        "Finance":finance,
        'Politics':politics
    }
    return render(request,"content/home.html",context)

class ArticleDetail(FormMixin,DetailView):
    template_name = 'content/detail.html'
    queryset = Article.objects.all()

    form_class = CommentForm
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        subscription = None
        pricing_tier = None
        fav = bool
        context = super(ArticleDetail,self).get_context_data(**kwargs)
        course = get_object_or_404(Article,slug=self.kwargs['slug'])
        posts = Article.objects.filter(category=course.category).exclude(slug=course.slug)[:3]
        if self.request.user.is_authenticated:
            if course.favourites.filter(id=self.request.user.profile.id).exists():
                    fav = True
        if  self.request.user != course.writer and  self.request.user.is_authenticated:        
            course.views +=1
            course.save()
        if self.request.user.is_authenticated:
            subscription = self.request.user.subscription
            pricing_tier  = subscription.pricing
    
        context.update({
            "has_permission":pricing_tier in course.pricing_tiers.all(),
            "fav":fav,
            "posts":posts
        })    
        return context
   

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        course = get_object_or_404(Article,slug=self.kwargs['slug'])
        instance = form.save(commit=False)
        instance.profile = self.request.user.profile
        instance.post = course
        instance.save()
        self.article = instance
        messages.success(self.request,"comment submitted")
        return super(ArticleDetail,self).form_valid(form)        
 
 

    def get_success_url(self):
        return reverse("article-detail", kwargs={"slug":self.kwargs["slug"]})

def articlePages(request,slug):
    posts = Article.objects.filter(category=slug).order_by('-created_date')
    paginator = Paginator(posts,15)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
        "posts":posts,
        'moreposts':paged_listings,


    }
    return render(request,"content/category-single.html",context)


class contactView(CreateView):
    template_name = "content/contact.html"
    form_class = ContactForm 


    def get_success_url(self):
        messages.success(self.request, 'Your details have been submitted.')
        return reverse('contact')  
        
@login_required
def favourite_add(request,slug):
    post = get_object_or_404(Article,slug=slug)
    if post.favourites.filter(id=request.user.profile.id).exists():
            post.favourites.remove(request.user.profile)
            messages.success(request,"Removed from saved articles!")


    else:
            post.favourites.add(request.user.profile)
            messages.success(request,"Added to saved articles!")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
        new  = Article.objects.filter(favourites=request.user.profile)
        context={'new':new}
        return render(request,'user/favourites.html',context)

def search(request):
    queryset_list=Article.objects.order_by('-created_date')
    # keyword
    if 'search' in request.GET:
        article=request.GET['search']
        if article:
            queryset_list = queryset_list.filter(title__icontains=article)
    # city
    context={
        'articles':queryset_list,
        'values':request.GET,
    }

    return render(request,'content/search.html',context)    

class BecomeAWriter(LoginRequiredMixin,CreateView):
    template_name = "content/become.html"
    form_class = BecomeWriterForm 


    def get_success_url(self):
        messages.success(self.request, 'Thank you for applying we will get back to you shortly')
        return reverse('becomeawriter')  