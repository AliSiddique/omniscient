from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from payment.models import Pricing
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import stripe
from user.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
stripe.api_key= settings.STRIPE_SECRET_KEY
class Subscribe(TemplateView):
    template_name = "payment/subscribe.html"
 

class PaymentView(LoginRequiredMixin,TemplateView):
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


@csrf_exempt
def webhook(request):
    webhook_secret = settings.WEBHOOK_SECRET
    payload = request.body

    # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
    signature = request.META["HTTP_STRIPE_SIGNATURE"]
    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=signature, secret=webhook_secret)
        data = event['data']
    except Exception as e:
        return e
        
    # Get the type of webhook event sent - used to check the status of PaymentIntents.
    event_type = event['type']
    data_object = data['object']

    if event_type == 'invoice.paid':

        webhook_object = data["object"]
        stripe_customer_id = webhook_object["customer"]

        stripe_sub = stripe.Subscription.retrieve(webhook_object["subscription"])
        stripe_price_id = stripe_sub["plan"]["id"]

        pricing = Pricing.objects.get(stripe_price_id=stripe_price_id)

        user = User.objects.get(stripe_customer_id=stripe_customer_id)
        user.subscription.status = stripe_sub["status"]
        user.subscription.stripe_subscription_id = webhook_object["subscription"]
        user.subscription.pricing = pricing
        user.subscription.save()

    if event_type == 'invoice.finalized':
        # If you want to manually send out invoices to your customers
        # or store them locally to reference to avoid hitting Stripe rate limits.
        print(data)

    if event_type == 'customer.subscription.deleted':
        # handle subscription cancelled automatically based
        # upon your subscription settings. Or if the user cancels it.
        webhook_object = data["object"]
        stripe_customer_id = webhook_object["customer"]
        stripe_sub = stripe.Subscription.retrieve(webhook_object["id"])
        user = User.objects.get(stripe_customer_id=stripe_customer_id)
        user.subscription.status = stripe_sub["status"]
        user.subscription.save()

    if event_type == 'customer.subscription.trial_will_end':
        # Send notification to your user that the trial will end
        print(data)

    if event_type == 'customer.subscription.updated':
        print(data)

    return HttpResponse()


class RetryInvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        try:

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

            invoice = stripe.Invoice.retrieve(
                data['invoiceId'],
                expand=['payment_intent'],
            )
            data = {}
            data.update(invoice)

            return Response(data)
        except Exception as e:

            return Response({
                "error": {'message': str(e)}
            })
