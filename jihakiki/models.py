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


# Model for holding Mwananchi Jihakiki profile during registration
class TempMwananchi(models.Model):
    """Model for holding Mwananchi Jihakiki profile during registration"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200, null=True)
    kitongoji = models.CharField(max_length=200, null=True)
    mtaa_kijiji = models.CharField(max_length=200, null=True)
    kata = models.CharField(max_length=200, null=True)
    id_card = models.CharField(max_length=20, null=True)
    id_number = models.IntegerField(unique=True, null=True)
    pin = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    status = models.CharField(max_length=20)


# Model for storing Mwananchi Jihakiki complete profile
class Mwananchi(models.Model):
    """Model for storing Mwananchi Jihakiki complete profile"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    kitongoji = models.CharField(max_length=200)
    mtaa_kijiji = models.CharField(max_length=200)
    kata = models.CharField(max_length=200)
    id_card = models.CharField(max_length=20)
    id_number = models.IntegerField(unique=True)
    pin = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    is_active = models.CharField(max_length=20)
    verification_status = models.CharField(max_length=20)
    mjumbe_id = models.CharField(max_length=13, null=True)
    date_mjumbe_verified = models.DateTimeField(auto_now_add=True, null=True)
    barua_id = models.IntegerField(null=True)
    veo_id = models.CharField(max_length=13, null=True)
    date_veo_verified = models.DateTimeField(auto_now_add=True, null=True)


# Model for holding Mjumbe Jihakiki profile during registration
class TempMjumbe(models.Model):
    """Model for holding Mjumbe Jihakiki profile during registration"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200, null=True)
    shina = models.IntegerField(null=True)
    kitongoji = models.CharField(max_length=200, null=True)
    mtaa_kijiji = models.CharField(max_length=200, null=True)
    kata = models.CharField(max_length=200, null=True)
    id_card = models.CharField(max_length=20, null=True)
    id_number = models.IntegerField(unique=True, null=True)
    pin = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    status = models.CharField(max_length=20)

# Model for storing Mjumbe Jihakiki complete profile
class Mjumbe(models.Model):
    """Model for storing Mjumbe Jihakiki complete profile"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200)
    shina = models.IntegerField()
    kitongoji = models.CharField(max_length=200)
    mtaa_kijiji = models.CharField(max_length=200)
    kata = models.CharField(max_length=200)
    id_card = models.CharField(max_length=20)
    id_number = models.IntegerField(unique=True)
    pin = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    is_active = models.CharField(max_length=20)
    verification_status = models.CharField(max_length=20)
    veo_id = models.CharField(max_length=13, null=True)
    date_veo_verified = models.DateTimeField(auto_now_add=True, null=True)


# Model for holding VEO Jihakiki profile during registration
class TempVeo(models.Model):
    """Model for holding VEO Jihakiki profile during registration"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200, null=True)
    mtaa_kijiji = models.CharField(max_length=200, null=True)
    kata = models.CharField(max_length=200, null=True)
    id_card = models.CharField(max_length=20, null=True)
    id_number = models.IntegerField(unique=True, null=True)
    pin = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    status = models.CharField(max_length=20)


# Model for storing VEO Jihakiki complete profile
class Veo(models.Model):
    """Model for storing VEO Jihakiki complete profile"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200)
    mtaa_kijiji = models.CharField(max_length=200)
    kata = models.CharField(max_length=200)
    id_card = models.CharField(max_length=20)
    id_number = models.IntegerField(unique=True)
    pin = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()
    is_active = models.CharField(max_length=20)
    verification_status = models.CharField(max_length=20)
    weo_id = models.CharField(max_length=13, null=True)
    date_weo_verified = models.DateTimeField(auto_now_add=True, null=True)


# Model for storing WEO Jihakiki complete data
class Weo(models.Model):
    """Model for storing WEO Jihakiki complete data"""
    id = models.CharField(primary_key=True, max_length=13)
    phone = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=200)
    kata = models.CharField(max_length=200)
    id_card = models.CharField(max_length=20)
    id_number = models.IntegerField(unique=True)
    pin = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.CharField(max_length=20)


# Model for storing Barua from Mjumbe with no phone for Jihakiki data
class Barua(models.Model):
    """Model for storing Barua from Mjumbe with no phone for Jihakiki data"""
    veo_id = models.CharField(max_length=13)
    mwananchi_id = models.CharField(max_length=13, null=True)
    reference = models.CharField(unique=True, max_length=200, null=True)
    mjumbe_name = models.CharField(max_length=200, null=True)
    shina = models.IntegerField(null=True)
    kitongoji = models.CharField(max_length=200, null=True)
    mtaa_kijiji = models.CharField(max_length=200)
    kata = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)


# Model for storing Msimbo (Auto Generated PIN) used in various verification processes
class Pin(models.Model):
    """Model for storing Msimbo (Auto Generated PIN) used in various verification processes"""
    pin = models.CharField(max_length=6)
    generator_id = models.CharField(max_length=13)
    client_id = models.CharField(max_length=13)
    date_generated = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    date_used = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)


# Model for storing keywords and messages that are sent back to users
# when interacting with the system. All the questions.
class KeywordMessage(models.Model):
    """
    Model for storing conversation, flag, validation, and success messages
    that are sent back to users when interacting with the system.
    """
    keyword = models.CharField(max_length=50)
    message_type = models.CharField(max_length=50)
    message = models.TextField(max_length=918)
    step = models.IntegerField()
    project = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    member = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)


# Model for storing all postal code including wards, villages/streets and vitongoji
class PostCode(models.Model):
    """Model for storing all postal codes including wards, mtaa/vijiji and vitongoji"""
    council_postcode = models.IntegerField()
    district = models.CharField(max_length=200)
    district_postcode = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    ward_postcode = models.CharField(max_length=200)
    old_ward_postcode = models.CharField(max_length=200)
    mtaa_kijiji = models.CharField(max_length=200)
    kitongoji = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)