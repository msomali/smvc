# Test Telerivet Webhook API
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import TempMwananchi, Mwananchi, KeywordMessage
from django.db.models import Q, F

import json
import random

# Telerivet REST API
# The code below sends an SMS message via Telerivet:
def message(msg, recepient):

    from jihakiki import telerivet

    API_KEY = 'c7fAkAuMy8a6aUZQWyNNyYXSutXuszcV'
    PROJECT_ID = 'PJ592866ba523f191f'

    tr = telerivet.API(API_KEY)
    project = tr.initProjectById(PROJECT_ID)

    sent_msg = project.sendMessage(
        content = str(msg),
        to_number = str(recepient),
    )

    return HttpResponse('executed')


# Telerivet Webhook API
# The code below receives incoming message from Telerivet
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

        # Initials
        postcode = "999"
        randno = random.randint(10000, 99999)
        status_unverified = "Unverified"
        status_partial = "Partial"
        status_complete = "Complete"
        is_active = "Yes"
        mncID = "MNC-"+postcode+"-"+str(randno)
        mjbID = "MJB-"+postcode+"-"+str(randno)
        veoID = "VEO-"+postcode+"-"+str(randno)
        weoID = "WEO-"+postcode+"-"+str(randno)
        step = 1

        # Queries
        qry_mwananchi = Mwananchi.objects.filter(phone__exact=from_number)
        qry_temp_mwananchi = TempMwananchi.objects.filter(phone__exact=from_number)

        if qry_mwananchi:
            qry_mwananchi = Mwananchi.objects.get(phone=from_number)

            if qry_mwananchi.verification_status=="Unverified":
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Umeshajisajili katika mfumo huu. Tafadhali wasiliana na mjumbe au mtendaji wako kwa uhakiki."}
                    ]
                }), 'application/json')

            else:
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Karibu JIHAKIKI: "+qry_mwananchi.name+"\n"+
                                    "1. Wasifu wako.\n"+
                                    "2. Mawasiliano ya uongozi wa mtaa/kijiji/kitongoji chako.\n"+
                                    "3. Mawasiliano ya uongozi wa kata yako."
                        }
                    ]
                }), 'application/json')

        elif qry_temp_mwananchi:
            qry_temp_mwananchi = TempMwananchi.objects.get(phone=from_number)

            # Save Responses
            if qry_temp_mwananchi.step==1:
                qry_temp_mwananchi.name = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==2:
                qry_temp_mwananchi.occupation = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==3:
                qry_temp_mwananchi.kitongoji = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==4:
                qry_temp_mwananchi.mtaa_kijiji = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==5:
                qry_temp_mwananchi.kata = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==6:
                qry_temp_mwananchi.id_card = content
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==7:

                # Check ID
                if len(content)<=20 and content.isdigit():
                    qry_temp_mwananchi.id_number = int(content)
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya kitambulisho uliyoingiza sio sahihi. Hakikisha unaingiza tarakimu pekee."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwananchi.step==8:

                # Check PIN Length & Data Type
                if len(content)==4 and content.isdigit():
                    qry_temp_mwananchi.pin = int(content)
                    qry_temp_mwananchi.status = status_complete
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()

                    # Send Data to Mwananchi Table (qry_tu/qry_mw)
                    qry_temp_mwananchi = TempMwananchi.objects.get(phone=from_number)
                    qry_mwananchi = Mwananchi.objects.create(
                                                        id=qry_temp_mwananchi.id,
                                                        phone=qry_temp_mwananchi.phone,
                                                        name=qry_temp_mwananchi.name,
                                                        occupation=qry_temp_mwananchi.occupation,
                                                        kitongoji=qry_temp_mwananchi.kitongoji,
                                                        mtaa_kijiji=qry_temp_mwananchi.mtaa_kijiji,
                                                        kata=qry_temp_mwananchi.kata,
                                                        id_card=qry_temp_mwananchi.id_card,
                                                        id_number=qry_temp_mwananchi.id_number,
                                                        pin=qry_temp_mwananchi.pin,
                                                        step=step,
                                                        is_active=is_active,
                                                        verification_status=status_unverified
                                                    )

                    # Delete Data from Temp User Table (qry_tu)
                    qry_temp_mwananchi.delete()

                    # Send SMS to other person
                    message("Delivered", "+255715908000")

                    # (qry_mw)
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Usajili wako wa awali umekamilika."+
                                        "Nambari yako ya usajili ni "+qry_mwananchi.id+
                                        ".\n\n"+
                                        "Tafadhali wasiliana na mjumbe wako kwa uhakiki."
                                        }
                        ]
                    }), 'application/json')
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya siri uliyoingiza sio sahihi. Hakikisha umeingiza tarakimu 4 tu."}
                        ]
                    }), 'application/json')

            else:
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Invalid Step! Contact System Admin!"}
                    ]
                }), 'application/json')

            qry_keyword_message = KeywordMessage.objects.get(step=qry_temp_mwananchi.step)

            return HttpResponse(json.dumps({
                'messages': [
                    {'content': qry_keyword_message.message}
                ]
            }), 'application/json')

        else:
            # Capture Jihakiki Keyword
            keyword = content.split(' ', maxsplit=1)

            if keyword[0] in ["Jihakiki", "jihakiki", "JIHAKIKI"]:
                # (qryy/qryy)
                qry_temp_mwananchi = TempMwananchi.objects.create(
                                                id=mncID,
                                                phone=from_number,
                                                step=step,
                                                status=status_partial
                                            )
                qry_temp_mwananchi.save()

                # Query the Respective Message (qryy)
                qry_keyword_message = KeywordMessage.objects.get(step=qry_temp_mwananchi.step)

                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': qry_keyword_message.message}
                    ]
                }), 'application/json')

        return HttpResponse(json.dumps({
            'messages': [
                {'content': "Thanks for your message!"}
            ]
        }), 'application/json')