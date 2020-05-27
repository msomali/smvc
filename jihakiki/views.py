from django.shortcuts import render

# Test Github Webhook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Test Github Webhook
@csrf_exempt
def hello(request):
    return HttpResponse('pong')