from django.db import models

# Create your models here.
class SentMessages(models.Model):
    sender = models.CharField(default='System', max_length=13, blank=True)
    recipient = models.CharField(max_length=13, help_text='Enter Recipient Phone Number')
    message = models.TextField(max_length=480, help_text='Enter Your Messaage Here')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)


class ReceivedMessages(models.Model):
    sender = models.CharField(max_length=13)
    recipient = models.CharField(default='System', max_length=13, blank=True)
    message = models.TextField(max_length=480)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)