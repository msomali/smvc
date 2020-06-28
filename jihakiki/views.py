# Test Telerivet Webhook API
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import (TempMwananchi, TempMjumbe, TempMwenyekiti, TempVeo,
                    Mwananchi, Mjumbe, Mwenyekiti, Veo, Weo, Barua, Pin,
                    KeywordMessage, PostCode)
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
        mktID = "MKT-"+postcode+"-"+str(randno)
        veoID = "VEO-"+postcode+"-"+str(randno)
        step = 1
        project = "Jihakiki"
        service = "Usajili"
        member_mwananchi = "Mwananchi"
        member_mjumbe = "Mjumbe"
        member_mwenyekiti = "Mwenyekiti"
        member_mtendaji = "Mtendaji"
        message_type = "Convo"

        # Check Queries
        # Mwananchi Check Queries
        qry_mwananchi = Mwananchi.objects.filter(phone__exact=from_number)
        qry_temp_mwananchi = TempMwananchi.objects.filter(phone__exact=from_number)

        # Mjumbe Check Queries
        qry_mjumbe = Mjumbe.objects.filter(phone__exact=from_number)
        qry_temp_mjumbe = TempMjumbe.objects.filter(phone__exact=from_number)

        # Mwenyekiti Check Queries
        qry_mwenyekiti = Mwenyekiti.objects.filter(phone__exact=from_number)
        qry_temp_mwenyekiti = TempMwenyekiti.objects.filter(phone__exact=from_number)

        # VEO Check Queries
        qry_veo = Veo.objects.filter(phone__exact=from_number)
        qry_temp_veo = TempVeo.objects.filter(phone__exact=from_number)

        # WEO Check Queries
        qry_weo = Weo.objects.filter(phone__exact=from_number)

        # Mwananchi Registered Query
        if qry_mwananchi:
            qry_mwananchi = qry_mwananchi.get(phone=from_number)

            # Capture Functional Keyword
            keyword = content.split(' ', maxsplit=2)

            if qry_mwananchi.verification_status=="Unverified":
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Umeshajisajili katika mfumo huu. Tafadhali wasiliana na mjumbe wako wa shina au afisa mtendaji wako wa mtaa kwa uhakiki."}
                    ]
                }), 'application/json')

            elif qry_mwananchi.verification_status=="Verified" and qry_mwananchi.is_active=="Yes" and keyword[0].upper()=="JIHAKIKI":
                if content.strip().isdigit()==False:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Karibu JIHAKIKI: "+qry_mwananchi.name+"\n"+
                                        "1. Wasifu wako.\n"+
                                        "2. Mawasiliano ya uongozi wa mtaa/kijiji/kitongoji chako.\n"+
                                        "3. Mawasiliano ya uongozi wa kata yako."
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==1:
                    # Return wasifu
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Wasifu wako:\n"+
                                        "Namba: "+qry_mwananchi.id+"\n"+
                                        "Jina: "+qry_mwananchi.name+"\n"+
                                        "Simu: "+qry_mwananchi.phone+"\n"+
                                        "Kazi: "+qry_mwananchi.occupation+"\n"+
                                        "Kitambulisho: "+qry_mwananchi.id_card+"\n"+
                                        "Kata: "+qry_mwananchi.kata+"\n"+
                                        "Mtaa/Kijiji: "+qry_mwananchi.mtaa_kijiji+"\n"+
                                        "Kitongoji: "+qry_mwananchi.kitongoji+"\n"+
                                        "Jihakiki: "+qry_mwananchi.verification_status
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==2:
                    # Return mawasiliano ya uongozi wa mtaa/kijiji/kitongoji
                    qry_mjumbe = Mjumbe.objects.get(kata__exact=qry_mwananchi.kata, mtaa_kijiji__exact=qry_mwananchi.mtaa_kijiji, kitongoji__exact=qry_mwananchi.kitongoji, verification_status__exact="Verified", is_active__exact="Yes")

                    qry_mwenyekiti = Mwenyekiti.objects.get(kata__exact=qry_mwananchi.kata, mtaa_kijiji__exact=qry_mwananchi.mtaa_kijiji, verification_status__exact="Verified", is_active__exact="Yes")

                    qry_veo = Veo.objects.get(kata__exact=qry_mwananchi.kata, mtaa_kijiji__exact=qry_mwananchi.mtaa_kijiji, verification_status__exact="Verified", is_active__exact="Yes")

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Mjumbe:\n"+
                                        "Jina: "+qry_mjumbe.name+"\n"+
                                        "Simu: "+qry_mjumbe.phone+"\n\n"+
                                        "Mwenyekiti:\n"+
                                        "Jina: "+qry_mwenyekiti.name+"\n"+
                                        "Simu: "+qry_mwenyekiti.phone+"\n\n"+
                                        "Mtendaji:\n"+
                                        "Jina: "+qry_veo.name+"\n"+
                                        "Simu: "+qry_veo.phone
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==3:
                    # Return mawasiliano ya uongozi wa kata
                    qry_weo = Weo.objects.get(kata__exact=qry_mwananchi.kata, is_active__exact="Yes")

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Mtendaji:\n"+
                                        "Jina: "+qry_weo.name+"\n"+
                                        "Simu: "+qry_weo.phone
                            }
                        ]
                    }), 'application/json')

                else:
                    pass

            else:
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Samahani, akaunti yako imesitishwa. Tafadhali wasiliana na mtendaji wa mtaa wako kurudisha akaunti yako."}
                    ]
                }), 'application/json')

        # Mwananchi Registration Queries
        elif qry_temp_mwananchi:
            qry_temp_mwananchi = TempMwananchi.objects.get(phone=from_number)

            # Save Responses
            if qry_temp_mwananchi.step==1:
                qry_temp_mwananchi.name = content.title()
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()
            elif qry_temp_mwananchi.step==2:
                qry_temp_mwananchi.occupation = content.title()
                qry_temp_mwananchi.step += 1
                qry_temp_mwananchi.save()

            elif qry_temp_mwananchi.step==3:
                # Check Ward
                qry_ward = PostCode.objects.filter(ward__exact=content.title()).distinct()
                if qry_ward:
                    qry_temp_mwananchi.kata = content.title()
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kata uliloingiza halipo. Hakikisha jina la kata na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwananchi.step==4:
                # Check Mtaa/Kijiji
                qry_mtaa_kijiji = PostCode.objects.filter(mtaa_kijiji__exact=content.title(), ward__exact=qry_temp_mwananchi.kata).distinct()
                if qry_mtaa_kijiji:
                    qry_temp_mwananchi.mtaa_kijiji = content.title()
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la mtaa/kijiji uliloingiza halipo. Hakikisha jina la mtaa/kijiji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwananchi.step==5:
                # Check Kitongoji
                qry_kitongoji = PostCode.objects.filter(kitongoji__exact=content.title(), mtaa_kijiji__exact=qry_temp_mwananchi.mtaa_kijiji, ward__exact=qry_temp_mwananchi.kata).distinct()
                if qry_kitongoji:
                    qry_temp_mwananchi.kitongoji = content.title()
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitongoji uliloingiza halipo. Hakikisha jina la kitongoji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwananchi.step==6:
                # Check ID Name
                if content.upper() in ["NIDA", "KURA", "LESENI"]:
                    qry_temp_mwananchi.id_card = content.title()
                    qry_temp_mwananchi.step += 1
                    qry_temp_mwananchi.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitambulisho uliloingiza sio sahihi. Vitambulisho vinavyokubalika ni NIDA, Kura na Leseni tu."}
                        ]
                    }), 'application/json')

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

                    # Send Data to Mwananchi Table
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

                    # Delete Data from TempMwananchi Table
                    qry_temp_mwananchi.delete()

                    # Notify Mwenyekiti via SMS on completion of Mwananchi registration
                    qry_mwenyekiti = Mwenyekiti.objects.filter(kata__exact=qry_mwananchi.kata, mtaa_kijiji__exact=qry_mwananchi.mtaa_kijiji, is_active__exact="Yes")
                    qry_mwenyekiti = qry_mwenyekiti.get(verification_status__exact="Verified")

                    if qry_mwenyekiti:
                        message_to_mwenyekiti = "Habari, mwananchi amejisajili.\n" \
                            "Namba: "+qry_mwananchi.id+"\n" \
                                "Jina: "+qry_mwananchi.name+"\n" \
                                    "Kata: "+qry_mwananchi.kata+"\n" \
                                        "Mtaa/Kijiji: "+qry_mwananchi.mtaa_kijiji+"\n" \
                                            "Kitongoji: "+qry_mwananchi.kitongoji

                        message(message_to_mwenyekiti, qry_mwenyekiti.phone)
                    else:
                        pass

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Usajili wako wa awali umekamilika."+
                                        "Nambari yako ya usajili ni "+qry_mwananchi.id+
                                        ".\n\n"+
                                        "Tafadhali wasiliana na mjumbe wako wa shina kwa uhakiki."
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

            qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mwananchi.step)
            qry_keyword_message = qry_keyword_message.filter(project=project)
            qry_keyword_message = qry_keyword_message.filter(service=service)
            qry_keyword_message = qry_keyword_message.filter(member=member_mwananchi)
            qry_keyword_message = qry_keyword_message.get(message_type=message_type)

            return HttpResponse(json.dumps({
                'messages': [
                    {'content': qry_keyword_message.message}
                ]
            }), 'application/json')


        # Mjumbe Registered Query
        elif qry_mjumbe:
            qry_mjumbe = qry_mjumbe.get(phone=from_number)

            # Capture Functional Keyword
            keyword = content.split(' ', maxsplit=2)

            if qry_mjumbe.verification_status=="Unverified":
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Umeshajisajili katika mfumo huu. Tafadhali wasiliana na afisa mtendaji wako wa mtaa kwa uhakiki."}
                    ]
                }), 'application/json')

            # Services available under Mjumbe Keyword
            elif qry_mjumbe.verification_status=="Verified" and qry_mjumbe.is_active=="Yes" and keyword[0].upper()=="MJUMBE":
                if content.strip().isdigit()==False:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Karibu JIHAKIKI: "+qry_mjumbe.name+"\n"+
                                        "1. Wasifu wako.\n"+
                                        "2. Mawasiliano ya uongozi wa mtaa/kijiji chako.\n"+
                                        "3. Mawasiliano ya uongozi wa kata yako."
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==1:
                    # Return wasifu
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Wasifu wako:\n"+
                                        "Namba: "+qry_mjumbe.id+"\n"+
                                        "Jina: "+qry_mjumbe.name+"\n"+
                                        "Simu: "+qry_mjumbe.phone+"\n"+
                                        "Kitambulisho: "+qry_mjumbe.id_card+"\n"+
                                        "Kata: "+qry_mjumbe.kata+"\n"+
                                        "Mtaa/Kijiji: "+qry_mjumbe.mtaa_kijiji+"\n"+
                                        "Kitongoji: "+qry_mjumbe.kitongoji+"\n"+
                                        "Shina: "+qry_mjumbe.shina+"\n"+
                                        "Jihakiki: "+qry_mjumbe.verification_status
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==2:
                    # Return mawasiliano ya uongozi wa mtaa/kijiji/kitongoji
                    qry_mwenyekiti = Mwenyekiti.objects.get(kata__exact=qry_mjumbe.kata, mtaa_kijiji__exact=qry_mjumbe.mtaa_kijiji, verification_status__exact="Verified", is_active__exact="Yes")

                    qry_veo = Veo.objects.get(kata__exact=qry_mjumbe.kata, mtaa_kijiji__exact=qry_mjumbe.mtaa_kijiji, verification_status__exact="Verified", is_active__exact="Yes")

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Mwenyekiti:\n"+
                                        "Jina: "+qry_mwenyekiti.name+"\n"+
                                        "Simu: "+qry_mwenyekiti.phone+"\n\n"+
                                        "Mtendaji:\n"+
                                        "Jina: "+qry_veo.name+"\n"+
                                        "Simu: "+qry_veo.phone
                            }
                        ]
                    }), 'application/json')

                elif int(content.strip())==3:
                    # Return mawasiliano ya uongozi wa kata
                    qry_weo = Weo.objects.get(kata__exact=qry_mjumbe.kata, is_active__exact="Yes")

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Mtendaji:\n"+
                                        "Jina: "+qry_weo.name+"\n"+
                                        "Simu: "+qry_weo.phone
                            }
                        ]
                    }), 'application/json')

                else:
                    pass

            # Review Service
            elif qry_mjumbe.verification_status=="Verified" and qry_mjumbe.is_active=="Yes" and keyword[0].upper()=="HAKIKI":
                # Check PIN
                if int(keyword[2])==qry_mjumbe.pin:
                    qry_mwananchi = Mwananchi.objects.get(id__exact=keyword[1])
                    # Check for mwananchi
                    if qry_mwananchi:
                        return HttpResponse(json.dumps({
                            'messages': [
                                {'content': "Yupo"}
                            ]
                        }), 'application/json')
                #         # Check Mwananchi Active and Verification status
                #         if qry_mwananchi.is_active=="Yes" and qry_mwananchi.verification_status=="Unverified":
                #             qry_mwananchi.step += 1
                #             qry_mwananchi.mjumbe_id = qry_mjumbe.id
                #             qry_mwananchi.save()
                #         else:
                #             return HttpResponse(json.dumps({
                #                 'messages': [
                #                     {'content': "Samahani, namba ya usajili ya mwananchi imesitishwa au imeshahakikiwa."}
                #                 ]
                #             }), 'application/json')
                    else:
                        return HttpResponse(json.dumps({
                            'messages': [
                                {'content': "Samahani, namba ya usajili ya mwananchi haipo."}
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
                        {'content': "Samahani, akaunti yako imesitishwa. Tafadhali wasiliana na mtendaji wa mtaa wako kurudisha akaunti yako."}
                    ]
                }), 'application/json')

        # Mjumbe Registration Queries
        elif qry_temp_mjumbe:
            qry_temp_mjumbe = TempMjumbe.objects.get(phone=from_number)

            # Save Responses
            if qry_temp_mjumbe.step==1:
                qry_temp_mjumbe.name = content.title()
                qry_temp_mjumbe.step += 1
                qry_temp_mjumbe.save()

            elif qry_temp_mjumbe.step==2:
                # Check Ward
                qry_ward = PostCode.objects.filter(ward__exact=content.title()).distinct()
                if qry_ward:
                    qry_temp_mjumbe.kata = content.title()
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kata uliloingiza halipo. Hakikisha jina la kata na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==3:
                # Check Mtaa/Kijiji
                qry_mtaa_kijiji = PostCode.objects.filter(mtaa_kijiji__exact=content.title(), ward__exact=qry_temp_mjumbe.kata).distinct()
                if qry_mtaa_kijiji:
                    qry_temp_mjumbe.mtaa_kijiji = content.title()
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la mtaa/kijiji uliloingiza halipo. Hakikisha jina la mtaa/kijiji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==4:
                # Check Kitongoji
                qry_kitongoji = PostCode.objects.filter(kitongoji__exact=content.title(), mtaa_kijiji__exact=qry_temp_mjumbe.mtaa_kijiji, ward__exact=qry_temp_mjumbe.kata).distinct()
                if qry_kitongoji:
                    qry_temp_mjumbe.kitongoji = content.title()
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitongoji uliloingiza halipo. Hakikisha jina la kitongoji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==5:

                # Check Shina Length & Data Type
                if len(content)<=3 and content.isdigit():
                    qry_temp_mjumbe.shina = content
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya shina uliyoingiza sio sahihi. Hakikisha umeingiza tarakimu zisizozidi 3 tu."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==6:

                # Check ID Name
                if content.upper() in ["NIDA", "KURA", "LESENI"]:
                    qry_temp_mjumbe.id_card = content.title()
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitambulisho uliloingiza sio sahihi. Vitambulisho vinavyokubalika ni NIDA, Kura na Leseni tu."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==7:

                # Check ID Number
                if len(content)<=20 and content.isdigit():
                    qry_temp_mjumbe.id_number = int(content)
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya kitambulisho uliyoingiza sio sahihi. Hakikisha unaingiza tarakimu pekee."}
                        ]
                    }), 'application/json')

            elif qry_temp_mjumbe.step==8:

                # Check PIN Length & Data Type
                if len(content)==4 and content.isdigit():
                    qry_temp_mjumbe.pin = int(content)
                    qry_temp_mjumbe.status = status_complete
                    qry_temp_mjumbe.step += 1
                    qry_temp_mjumbe.save()

                    # Send Data to Mjumbe Table
                    qry_temp_mjumbe = TempMjumbe.objects.get(phone=from_number)
                    qry_mjumbe = Mjumbe.objects.create(
                                                        id=qry_temp_mjumbe.id,
                                                        phone=qry_temp_mjumbe.phone,
                                                        name=qry_temp_mjumbe.name,
                                                        shina=qry_temp_mjumbe.shina,
                                                        kitongoji=qry_temp_mjumbe.kitongoji,
                                                        mtaa_kijiji=qry_temp_mjumbe.mtaa_kijiji,
                                                        kata=qry_temp_mjumbe.kata,
                                                        id_card=qry_temp_mjumbe.id_card,
                                                        id_number=qry_temp_mjumbe.id_number,
                                                        pin=qry_temp_mjumbe.pin,
                                                        step=step,
                                                        is_active=is_active,
                                                        verification_status=status_unverified
                                                    )

                    # Delete Data from TempMjumbe Table
                    qry_temp_mjumbe.delete()

                    # Notify VEO via SMS on completion of Mjumbe registration
                    qry_veo = Veo.objects.filter(kata__exact=qry_mjumbe.kata, mtaa_kijiji__exact=qry_mjumbe.mtaa_kijiji, is_active__exact="Yes")
                    qry_veo = qry_veo.get(verification_status__exact="Verified")

                    if qry_veo:
                        message_to_veo = "Habari, mjumbe amejisajili.\n" \
                            "Namba: "+qry_mjumbe.id+"\n" \
                                "Jina: "+qry_mjumbe.name+"\n" \
                                    "Kata: "+qry_mjumbe.kata+"\n" \
                                        "Mtaa/Kijiji: "+qry_mjumbe.mtaa_kijiji+"\n" \
                                            "Kitongoji: "+qry_mjumbe.kitongoji+"\n" \
                                                "Simu: "+qry_mjumbe.phone

                        message(message_to_veo, qry_veo.phone)
                    else:
                        pass

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Usajili wako wa awali umekamilika."+
                                        "Nambari yako ya usajili ni "+qry_mjumbe.id+
                                        ".\n\n"+
                                        "Tafadhali wasiliana na afisa mtendaji wako wa mtaa kwa uhakiki."
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
                # To be replaced by pass
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Invalid Step! Contact System Admin!"}
                    ]
                }), 'application/json')

            qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mjumbe.step)
            qry_keyword_message = qry_keyword_message.filter(project=project)
            qry_keyword_message = qry_keyword_message.filter(service=service)
            qry_keyword_message = qry_keyword_message.get(member=member_mjumbe)

            return HttpResponse(json.dumps({
                'messages': [
                    {'content': qry_keyword_message.message}
                ]
            }), 'application/json')


        # Mwenyekiti Registered Query
        elif qry_mwenyekiti:
            qry_mwenyekiti = Mwenyekiti.objects.get(phone=from_number)

            if qry_mwenyekiti.verification_status=="Unverified":
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Umeshajisajili katika mfumo huu. Tafadhali wasiliana na afisa mtendaji wako wa kata kwa uhakiki."}
                    ]
                }), 'application/json')

            else:
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Karibu JIHAKIKI: "+qry_mwenyekiti.name+"\n"+
                                    "1. Wasifu wako.\n"+
                                    "2. Mawasiliano ya uongozi wa kijiji/kitongoji chako.\n"+
                                    "3. Mawasiliano ya uongozi wa kata yako."
                        }
                    ]
                }), 'application/json')

        # Mwenyekiti Registration Queries
        elif qry_temp_mwenyekiti:
            qry_temp_mwenyekiti = TempMwenyekiti.objects.get(phone=from_number)

            # Save Responses
            if qry_temp_mwenyekiti.step==1:
                qry_temp_mwenyekiti.name = content.title()
                qry_temp_mwenyekiti.step += 1
                qry_temp_mwenyekiti.save()

            elif qry_temp_mwenyekiti.step==2:
                # Check Ward
                qry_ward = PostCode.objects.filter(ward__exact=content.title()).distinct()
                if qry_ward:
                    qry_temp_mwenyekiti.kata = content.title()
                    qry_temp_mwenyekiti.step += 1
                    qry_temp_mwenyekiti.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kata uliloingiza halipo. Hakikisha jina la kata na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwenyekiti.step==3:
                # Check Mtaa/Kijiji
                qry_mtaa_kijiji = PostCode.objects.filter(mtaa_kijiji__exact=content.title(), ward__exact=qry_temp_mwenyekiti.kata).distinct()
                if qry_mtaa_kijiji:
                    qry_temp_mwenyekiti.mtaa_kijiji = content.title()
                    qry_temp_mwenyekiti.step += 1
                    qry_temp_mwenyekiti.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la mtaa/kijiji uliloingiza halipo. Hakikisha jina la mtaa/kijiji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwenyekiti.step==4:

                # Check ID Name
                if content.upper() in ["NIDA", "KURA", "LESENI"]:
                    qry_temp_mwenyekiti.id_card = content.title()
                    qry_temp_mwenyekiti.step += 1
                    qry_temp_mwenyekiti.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitambulisho uliloingiza sio sahihi. Vitambulisho vinavyokubalika ni NIDA, Kura na Leseni tu."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwenyekiti.step==5:

                # Check ID
                if len(content)<=20 and content.isdigit():
                    qry_temp_mwenyekiti.id_number = int(content)
                    qry_temp_mwenyekiti.step += 1
                    qry_temp_mwenyekiti.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya kitambulisho uliyoingiza sio sahihi. Hakikisha unaingiza tarakimu pekee."}
                        ]
                    }), 'application/json')

            elif qry_temp_mwenyekiti.step==6:

                # Check PIN Length & Data Type
                if len(content)==4 and content.isdigit():
                    qry_temp_mwenyekiti.pin = int(content)
                    qry_temp_mwenyekiti.status = status_complete
                    qry_temp_mwenyekiti.step += 1
                    qry_temp_mwenyekiti.save()

                    # Send Data to Mwenyekiti Table
                    qry_temp_mwenyekiti = TempMwenyekiti.objects.get(phone=from_number)
                    qry_mwenyekiti = Mwenyekiti.objects.create(
                                                        id=qry_temp_mwenyekiti.id,
                                                        phone=qry_temp_mwenyekiti.phone,
                                                        name=qry_temp_mwenyekiti.name,
                                                        mtaa_kijiji=qry_temp_mwenyekiti.mtaa_kijiji,
                                                        kata=qry_temp_mwenyekiti.kata,
                                                        id_card=qry_temp_mwenyekiti.id_card,
                                                        id_number=qry_temp_mwenyekiti.id_number,
                                                        pin=qry_temp_mwenyekiti.pin,
                                                        step=step,
                                                        is_active=is_active,
                                                        verification_status=status_unverified
                                                    )

                    # Delete Data from TempMwenyekiti Table
                    qry_temp_mwenyekiti.delete()

                    # Notify WEO via SMS on completion of Mwenyekiti registration
                    qry_weo = Weo.objects.filter(kata__exact=qry_mwenyekiti.kata)
                    qry_weo = qry_weo.get(is_active__exact="Yes")

                    if qry_weo:
                        message_to_weo = "Habari, mwenyekiti amejisajili.\n" \
                            "Namba: "+qry_mwenyekiti.id+"\n" \
                                "Jina: "+qry_mwenyekiti.name+"\n" \
                                    "Kata: "+qry_mwenyekiti.kata+"\n" \
                                        "Mtaa/Kijiji: "+qry_mwenyekiti.mtaa_kijiji+"\n" \
                                                "Simu: "+qry_mwenyekiti.phone

                        message(message_to_weo, qry_weo.phone)
                    else:
                        pass

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Usajili wako wa awali umekamilika."+
                                        "Nambari yako ya usajili ni "+qry_mwenyekiti.id+
                                        ".\n\n"+
                                        "Tafadhali wasiliana na afisa mtendaji wako wa kata kwa uhakiki."
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
                # To be replaced by pass
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Invalid Step! Contact System Administrator!"}
                    ]
                }), 'application/json')

            qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mwenyekiti.step)
            qry_keyword_message = qry_keyword_message.filter(project=project)
            qry_keyword_message = qry_keyword_message.filter(service=service)
            qry_keyword_message = qry_keyword_message.get(member=member_mwenyekiti)

            return HttpResponse(json.dumps({
                'messages': [
                    {'content': qry_keyword_message.message}
                ]
            }), 'application/json')


        # VEO Registered Query
        elif qry_veo:
            qry_veo = Veo.objects.get(phone=from_number)

            if qry_veo.verification_status=="Unverified":
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Umeshajisajili katika mfumo huu. Tafadhali wasiliana na afisa mtendaji wako wa kata kwa uhakiki."}
                    ]
                }), 'application/json')

            else:
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Karibu JIHAKIKI: "+qry_veo.name+"\n"+
                                    "1. Wasifu wako.\n"+
                                    "2. Mawasiliano ya uongozi wa kijiji/kitongoji chako.\n"+
                                    "3. Mawasiliano ya uongozi wa kata yako."
                        }
                    ]
                }), 'application/json')

        # VEO Registration Queries
        elif qry_temp_veo:
            qry_temp_veo = TempVeo.objects.get(phone=from_number)

            # Save Responses
            if qry_temp_veo.step==1:
                qry_temp_veo.name = content.title()
                qry_temp_veo.step += 1
                qry_temp_veo.save()

            elif qry_temp_veo.step==2:
                # Check Ward
                qry_ward = PostCode.objects.filter(ward__exact=content.title()).distinct()
                if qry_ward:
                    qry_temp_veo.kata = content.title()
                    qry_temp_veo.step += 1
                    qry_temp_veo.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kata uliloingiza halipo. Hakikisha jina la kata na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_veo.step==3:
                # Check Mtaa/Kijiji
                qry_mtaa_kijiji = PostCode.objects.filter(mtaa_kijiji__exact=content.title(), ward__exact=qry_temp_veo.kata).distinct()
                if qry_mtaa_kijiji:
                    qry_temp_veo.mtaa_kijiji = content.title()
                    qry_temp_veo.step += 1
                    qry_temp_veo.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la mtaa/kijiji uliloingiza halipo. Hakikisha jina la mtaa/kijiji na urudie tena."}
                        ]
                    }), 'application/json')

            elif qry_temp_veo.step==4:

                # Check ID Name
                if content.upper() in ["NIDA", "KURA", "LESENI"]:
                    qry_temp_veo.id_card = content.title()
                    qry_temp_veo.step += 1
                    qry_temp_veo.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, jina la kitambulisho uliloingiza sio sahihi. Vitambulisho vinavyokubalika ni NIDA, Kura na Leseni tu."}
                        ]
                    }), 'application/json')

            elif qry_temp_veo.step==5:

                # Check ID
                if len(content)<=20 and content.isdigit():
                    qry_temp_veo.id_number = int(content)
                    qry_temp_veo.step += 1
                    qry_temp_veo.save()
                else:
                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Samahani, namba ya kitambulisho uliyoingiza sio sahihi. Hakikisha unaingiza tarakimu pekee."}
                        ]
                    }), 'application/json')

            elif qry_temp_veo.step==6:

                # Check PIN Length & Data Type
                if len(content)==4 and content.isdigit():
                    qry_temp_veo.pin = int(content)
                    qry_temp_veo.status = status_complete
                    qry_temp_veo.step += 1
                    qry_temp_veo.save()

                    # Send Data to VEO Table
                    qry_temp_veo = TempVeo.objects.get(phone=from_number)
                    qry_veo = Veo.objects.create(
                                                        id=qry_temp_veo.id,
                                                        phone=qry_temp_veo.phone,
                                                        name=qry_temp_veo.name,
                                                        mtaa_kijiji=qry_temp_veo.mtaa_kijiji,
                                                        kata=qry_temp_veo.kata,
                                                        id_card=qry_temp_veo.id_card,
                                                        id_number=qry_temp_veo.id_number,
                                                        pin=qry_temp_veo.pin,
                                                        step=step,
                                                        is_active=is_active,
                                                        verification_status=status_unverified
                                                    )

                    # Delete Data from TempVeo Table
                    qry_temp_veo.delete()

                    # Notify WEO via SMS on completion of VEO registration
                    qry_weo = Weo.objects.filter(kata__exact=qry_veo.kata)
                    qry_weo = qry_weo.get(is_active__exact="Yes")

                    if qry_weo:
                        message_to_weo = "Habari, mtendaji amejisajili.\n" \
                            "Namba: "+qry_veo.id+"\n" \
                                "Jina: "+qry_veo.name+"\n" \
                                    "Kata: "+qry_veo.kata+"\n" \
                                        "Mtaa/Kijiji: "+qry_veo.mtaa_kijiji+"\n" \
                                                "Simu: "+qry_veo.phone

                        message(message_to_weo, qry_weo.phone)
                    else:
                        pass

                    return HttpResponse(json.dumps({
                        'messages': [
                            {'content': "Usajili wako wa awali umekamilika."+
                                        "Nambari yako ya usajili ni "+qry_veo.id+
                                        ".\n\n"+
                                        "Tafadhali wasiliana na afisa mtendaji wako wa kata kwa uhakiki."
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
                # To be replaced by pass
                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': "Invalid Step! Contact System Administrator!"}
                    ]
                }), 'application/json')

            qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_veo.step)
            qry_keyword_message = qry_keyword_message.filter(project=project)
            qry_keyword_message = qry_keyword_message.filter(service=service)
            qry_keyword_message = qry_keyword_message.get(member=member_mtendaji)

            return HttpResponse(json.dumps({
                'messages': [
                    {'content': qry_keyword_message.message}
                ]
            }), 'application/json')


        # Verification Queries
        # Mwananchi Verification


        # New account creation for Mwananchi, Mjumbe & VEO
        else:
            # Capture Jihakiki Keyword
            keyword = content.split(' ', maxsplit=1)

            # Create Mwananchi Jihakiki Profile
            if keyword[0].upper()=="JIHAKIKI":
                qry_temp_mwananchi = TempMwananchi.objects.create(
                                                id=mncID,
                                                phone=from_number,
                                                step=step,
                                                status=status_partial
                                            )
                qry_temp_mwananchi.save()

                # Query the Respective Message
                qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mwananchi.step)
                qry_keyword_message = qry_keyword_message.filter(project=project)
                qry_keyword_message = qry_keyword_message.filter(service=service)
                qry_keyword_message = qry_keyword_message.filter(member=member_mwananchi)
                qry_keyword_message = qry_keyword_message.get(message_type=message_type)

                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': qry_keyword_message.message}
                    ]
                }), 'application/json')

            # Create Mjumbe Jihakiki Profile
            elif keyword[0].upper()=="MJUMBE":
                qry_temp_mjumbe = TempMjumbe.objects.create(
                                                id=mjbID,
                                                phone=from_number,
                                                step=step,
                                                status=status_partial
                                            )
                qry_temp_mjumbe.save()

                # Query the Respective Message
                qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mjumbe.step)
                qry_keyword_message = qry_keyword_message.filter(project=project)
                qry_keyword_message = qry_keyword_message.filter(service=service)
                qry_keyword_message = qry_keyword_message.get(member=member_mjumbe)

                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': qry_keyword_message.message}
                    ]
                }), 'application/json')

            # Create Mwenyekiti Jihakiki Profile
            elif keyword[0].upper()=="MWENYEKITI":
                qry_temp_mwenyekiti = TempMwenyekiti.objects.create(
                                                id=mktID,
                                                phone=from_number,
                                                step=step,
                                                status=status_partial
                                            )
                qry_temp_mwenyekiti.save()

                # Query the Respective Message
                qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_mwenyekiti.step)
                qry_keyword_message = qry_keyword_message.filter(project=project)
                qry_keyword_message = qry_keyword_message.filter(service=service)
                qry_keyword_message = qry_keyword_message.get(member=member_mwenyekiti)

                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': qry_keyword_message.message}
                    ]
                }), 'application/json')

            # Create Veo Jihakiki Profile
            elif keyword[0].upper()=="MTENDAJI":
                qry_temp_veo = TempVeo.objects.create(
                                                id=veoID,
                                                phone=from_number,
                                                step=step,
                                                status=status_partial
                                            )
                qry_temp_veo.save()

                # Query the Respective Message
                qry_keyword_message = KeywordMessage.objects.filter(step=qry_temp_veo.step)
                qry_keyword_message = qry_keyword_message.filter(project=project)
                qry_keyword_message = qry_keyword_message.filter(service=service)
                qry_keyword_message = qry_keyword_message.get(member=member_mtendaji)

                return HttpResponse(json.dumps({
                    'messages': [
                        {'content': qry_keyword_message.message}
                    ]
                }), 'application/json')

            else:
                # If no keywords were valid
                pass

        # To be replace by else pass for non keyword messages
        return HttpResponse(json.dumps({
            'messages': [
                {'content': "Thanks for your message!"}
            ]
        }), 'application/json')