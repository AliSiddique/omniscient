from django.urls import path

from .views import CancelSubscriptionView, UserSignupView,LoginView, UserSubscriptionView, editAccount, logout_view, profiles, single_profile,PasswordChangeView
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('signup/',UserSignupView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('writers/',profiles,name="profile-all"),
    path("single-profile/<slug>/",single_profile,name="single-profile"),
    path('passwordchange/',PasswordChangeView.as_view(),name="change-password"),
    path('profile/edit/',editAccount,name="editProfile"),
    path('profile/billing/<username>',UserSubscriptionView.as_view(),name="billing"),
    path('profile/billing/<username>/cancel',CancelSubscriptionView.as_view(),name="cancel"),

    path('logout/',logout_view,name="logout"),
    path('password-reset',PasswordResetView.as_view(template_name="user/passwordreset.html"),name="password-reset"),
    path('password-reset-done',PasswordResetDoneView.as_view(template_name="user/passwordresetdone.html"),name="password-reset-done"),
    path('password-reset-confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name="user/passwordresetconfirm.html"),name="password-reset-confirm"),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name="user/passwordresetcomplete.html"),name="password-reset-complete"),



]