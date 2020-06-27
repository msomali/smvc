from django.http import HttpResponse

# Telerivet REST API
# The code below sends an SMS message via Telerivet
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