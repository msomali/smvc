from django.shortcuts import render

# Test Github Webhook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Test Github Webhook
@csrf_exempt
def hello(request):
    return HttpResponse('pong')


# Test Telerivet Webhook API
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def webhook(request):
    webhook_secret = 'FEHULDR3HRKAFA7FXTXNNDPTR6EAQDZZ'

    if request.POST.get('secret') != webhook_secret:
        return HttpResponse("Invalid webhook secret", 'text/plain', 403)

    if request.POST.get('event') == 'incoming_message':
        content = request.POST.get('content')
        from_number = request.POST.get('from_number')
        phone_id = request.POST.get('phone_id')

        # do something with the message, e.g. send an autoreply

        if content == 'Zutrax':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Your Technology Partner!"}
                ]
            }), 'application/json')

        if content == 'JN Walid Abdul Amir Kambagha Mvungi':
            content1 = content[slice(2)]
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': content }
                ]
            }), 'application/json')

        return HttpResponse(json.dumps({
            'messages': [
                {'content': "Thanks for your message!"}
            ]
        }), 'application/json')

# Test Telerivet REST API
def message(request):
    # REST API
    # The code below sends an SMS message via Telerivet:
    # Temeke as Pilot

    from jihakiki import telerivet

    API_KEY = 'c7fAkAuMy8a6aUZQWyNNyYXSutXuszcV'
    PROJECT_ID = 'PJ592866ba523f191f'

    tr = telerivet.API(API_KEY)
    project = tr.initProjectById(PROJECT_ID)

    sent_msg = project.sendMessage(
        content = "hello world",
        to_number = "+255715908000",
    )

    return HttpResponse('executed')