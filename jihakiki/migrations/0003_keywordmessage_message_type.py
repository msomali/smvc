# Generated by Django 3.0.6 on 2020-06-17 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jihakiki', '0002_auto_20200616_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordmessage',
            name='message_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
