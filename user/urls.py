from django.urls import path

from .views import UserSignupView,LoginView, editAccount, logout_view, profiles, single_profile,PasswordChangeView
urlpatterns = [
    path('signup/',UserSignupView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('writers/',profiles,name="profile-all"),
    path("single-profile/<slug>/",single_profile,name="single-profile"),
    path('passwordchange/',PasswordChangeView.as_view(),name="change-password"),
    path('profile/edit/',editAccount,name="editProfile"),
    path('logout/',logout_view,name="logout")
]