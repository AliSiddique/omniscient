from django.urls import path
from .views import CreateCheckout, Subscribe,PaymentView

urlpatterns = [
    path('',Subscribe.as_view(),name="payment"),
    path('subscribe/<slug>/',PaymentView.as_view(),name="subscribe-plan"),
    path('create-subscription/',CreateCheckout.as_view(),name="create-subscription"),


]