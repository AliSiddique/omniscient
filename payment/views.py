from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from payment.models import Pricing
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe
# Create your views here.
stripe.api_key="sk_test_51LC3cmLF9bIFNtJzGGYAMuG72tTrBtWXQLNnBkhOIlRj5UT2s06e3gbKmGUdmopR3kiu8INiAagArvYavyOk5NMV00QOXvvP5d"
class Subscribe(TemplateView):
    template_name = "payment/subscribe.html"
 

class PaymentView(TemplateView):
    template_name = "payment/checkout.html"
    def get_context_data(self, **kwargs):
       context = super(PaymentView,self).get_context_data(**kwargs)
       pricing = get_object_or_404(Pricing,slug=kwargs["slug"])
       context.update({
        "pricing_tier":pricing,
        "STRIPE_PUBLIC_KEY":settings.STRIPE_PUBLIC_KEY
       })
       return context


class CreateCheckout(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        customer_id = request.user.stripe_customer_id
        print(customer_id)
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )

            data = {}
            data.update(subscription)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })
