from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView

from content.models import Article
# Create your views here.
def ArticleList(request):  
    economy = Article.objects.filter(category='Ec').filter(published=True)
    finance = Article.objects.filter(category='FI').filter(published=True)
    politics = Article.objects.filter(category='Po').filter(published=True)

    context={
        "Economy":economy,
        "Finance":finance,
        'Politics':politics
    }
    return render(request,"content/home.html",context)

class ArticleDetail(DetailView):
    template_name = 'content/detail.html'
    queryset = Article.objects.all()
    context_object_name = "post"
    fav = bool
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail,self).get_context_data(**kwargs)
        course = get_object_or_404(Article,slug=self.kwargs['slug'])
        if self.request.user.is_authenticated:
            if course.favourites.filter(id=self.request.user.profile.id).exists():
                fav = True
        course.views +=1
        course.save()

        subscription = self.request.user.subscription
        pricing_tier  = subscription.pricing
    
        context.update({
            "has_permission":pricing_tier in course.pricing_tiers.all()
        })    
        return context
   
    