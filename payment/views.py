from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def payment(request):
    return HttpResponse("Payment page")