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

        keyword = content.split(' ', maxsplit=1)

        # Intro
        if keyword[0] == 'Jihakiki':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Karibu JIHAKIKI, mfumo wa usajili wa wananchi katika serikali za mitaa wanamoishi.\nKujisajili, jibu ujumbe huu ukianza na neno AA.\nMfano: AA Walid Abdul Amir."}
                ]
            }), 'application/json')

        # Jina
        elif keyword[0] == 'AA':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi kazi yako ukianza na neno BB." }
                ]
            }), 'application/json')

        # Kazi
        elif keyword[0] == 'AA':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi kitongoji chako ukianza na neno CC." }
                ]
            }), 'application/json')

        # Kitongoji
        elif keyword[0] == 'CC':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi serikali ya mtaa ukianza na neno DD." }
                ]
            }), 'application/json')

        # Serikali ya Mtaa
        elif keyword[0] == 'DD':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi kata yako ukianza na neno EE." }
                ]
            }), 'application/json')

        # Kata
        elif keyword[0] == 'EE':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi namba yako ya NIDA ukianza na neno FF." }
                ]
            }), 'application/json')

        # NIDA
        elif keyword[0] == 'FF':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nHifadhi tarakimu zako 4 za siri yako ukianza na neno GG." }
                ]
            }), 'application/json')

        # PIN
        elif keyword[0] == 'GG':
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Umehifadhi: "+keyword[1]+"\nUmefikia mwisho wa dodoso la JIHAKIKI. Ahsante!." }
                ]
            }), 'application/json')

        # Exception
        else:
            return HttpResponse(json.dumps({
                'messages': [
                    {'content': "Samahani, umekosea mpangilio. Tafadhali hakiki ujumbe wako na kisha utume tena. Ahsante!"}
                ]
            }), 'application/json')

        # return HttpResponse(json.dumps({
        #     'messages': [
        #         {'content': "Thanks for your message!"}
        #     ]
        # }), 'application/json')

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