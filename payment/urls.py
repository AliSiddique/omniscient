from django.urls import path
from .views import CreateCheckout, RetryInvoiceView, Subscribe,PaymentView, webhook

urlpatterns = [
    path('',Subscribe.as_view(),name="payment"),
    path('subscribe/<slug>/',PaymentView.as_view(),name="subscribe-plan"),
    path('create-subscription/',CreateCheckout.as_view(),name="create-subscription"),
    path('webhook',webhook,name="webhook"),
    path('retry-invoice',RetryInvoiceView.as_view(),name="retry-invoice"),



]