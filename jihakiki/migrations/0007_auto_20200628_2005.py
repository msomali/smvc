# Generated by Django 3.0.6 on 2020-06-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jihakiki', '0006_mwenyekiti_tempmwenyekiti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mjumbe',
            name='date_veo_verified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='mwananchi',
            name='date_mjumbe_verified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='mwananchi',
            name='date_veo_verified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='mwenyekiti',
            name='date_weo_verified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date_used',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='veo',
            name='date_weo_verified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]