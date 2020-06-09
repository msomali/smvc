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


class TempUser(models.Model):
    mnc_id = models.CharField(primary_key=True, max_length=13)
    mnc_phone = models.CharField(unique=True, max_length=13)
    mnc_name = models.CharField(max_length=50, null=True)
    mnc_occupation = models.CharField(max_length=50, null=True)
    mnc_kitongoji = models.CharField(max_length=50, null=True)
    mnc_mtaa_kijiji = models.CharField(max_length=50, null=True)
    mnc_kata = models.CharField(max_length=50, null=True)
    mnc_id_card = models.CharField(max_length=50, null=True)
    mnc_id_number = models.IntegerField(unique=True, null=True)
    mnc_pin = models.IntegerField(null=True)
    mnc_date_time = models.DateTimeField(auto_now_add=True)
    mnc_step = models.IntegerField()
    mnc_status = models.CharField(max_length=50)


class Mwananchi(models.Model):
    mnc_id = models.CharField(primary_key=True, max_length=13)
    mnc_phone = models.CharField(unique=True, max_length=13)
    mnc_name = models.CharField(max_length=50)
    mnc_occupation = models.CharField(max_length=50)
    mnc_kitongoji = models.CharField(max_length=50)
    mnc_mtaa_kijiji = models.CharField(max_length=50)
    mnc_kata = models.CharField(max_length=50)
    mnc_id_card = models.CharField(max_length=50)
    mnc_id_number = models.IntegerField(unique=True)
    mnc_pin = models.IntegerField()
    mnc_date_time = models.DateTimeField(auto_now_add=True)
    mnc_step = models.IntegerField()
    mnc_status = models.CharField(max_length=50)


class KeyMessage(models.Model):
    keyword = models.CharField(max_length=50)
    statement = models.TextField()
    steps = models.IntegerField()