# Generated by Django 3.0.6 on 2020-06-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jihakiki', '0005_barua_keywordmessage_mjumbe_mwananchi_pin_tempmjumbe_tempmwananchi_tempveo_veo_weo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barua',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
