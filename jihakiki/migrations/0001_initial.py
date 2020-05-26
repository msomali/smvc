# Generated by Django 3.0.6 on 2020-05-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=13)),
                ('recipient', models.CharField(default='System', max_length=13)),
                ('message', models.TextField(max_length=480)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SentMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(blank=True, max_length=13)),
                ('recipient', models.CharField(help_text='Enter Recipient Phone Number', max_length=13)),
                ('message', models.TextField(help_text='Enter Your Messaage Here', max_length=480)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
