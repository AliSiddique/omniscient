from django.urls import path

from content.views import ArticleList,ArticleDetail
urlpatterns = [
    path('',ArticleList,name="article-list"),
    path('articles/<slug>',ArticleDetail.as_view(),name="article-detail")
]