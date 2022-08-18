from django.urls import path

from content.views import ArticleList,ArticleDetail, BecomeAWriter,articlePages, contactView, favourite_add, favourite_list, search
urlpatterns = [
    path('',ArticleList,name="article-list"),
    path('articles/<slug>',ArticleDetail.as_view(),name="article-detail"),
    path('category/<slug>/',articlePages,name="single-category"),
    path('contact/',contactView.as_view(),name="contact"),
    path('fav/<slug:slug>/',favourite_add,name="favourite_add"),
    path('profile/favourites/',favourite_list,name="favourites"),
    path('search/',search,name="search"),
    path('becomeawriter/',BecomeAWriter.as_view(),name="becomeawriter"),




]