# REST API
# The code below sends an SMS message via Telerivet:
# Temeke as Pilot

import telerivet

API_KEY = 'c7fAkAuMy8a6aUZQWyNNyYXSutXuszcV'
PROJECT_ID = 'PJ592866ba523f191f'

tr = telerivet.API(API_KEY)
project = tr.initProjectById(PROJECT_ID)

sent_msg = project.sendMessage(
    content = "hello world",
    to_number = "+255715908000",
)