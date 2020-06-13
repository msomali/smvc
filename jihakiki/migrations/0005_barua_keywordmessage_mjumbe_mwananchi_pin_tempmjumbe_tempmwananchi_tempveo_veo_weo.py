# Generated by Django 3.0.6 on 2020-06-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jihakiki', '0004_auto_20200526_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barua',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('veo_id', models.CharField(max_length=13)),
                ('mwananchi_id', models.CharField(max_length=13, null=True)),
                ('reference', models.CharField(max_length=200, null=True, unique=True)),
                ('mjumbe_name', models.CharField(max_length=200, null=True)),
                ('shina', models.IntegerField(null=True)),
                ('kitongoji', models.CharField(max_length=200, null=True)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=918)),
                ('step', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mjumbe',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('shina', models.IntegerField()),
                ('kitongoji', models.CharField(max_length=200)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('is_active', models.CharField(max_length=20)),
                ('verification_status', models.CharField(max_length=20)),
                ('veo_id', models.CharField(max_length=13, null=True)),
                ('date_veo_verified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mwananchi',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('kitongoji', models.CharField(max_length=200)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('is_active', models.CharField(max_length=20)),
                ('verification_status', models.CharField(max_length=20)),
                ('mjumbe_id', models.CharField(max_length=13, null=True)),
                ('date_mjumbe_verified', models.DateTimeField(auto_now_add=True, null=True)),
                ('barua_id', models.IntegerField(null=True)),
                ('veo_id', models.CharField(max_length=13, null=True)),
                ('date_veo_verified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pin', models.CharField(max_length=6)),
                ('generator_id', models.CharField(max_length=13)),
                ('client_id', models.CharField(max_length=13)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_used', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempMjumbe',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('shina', models.IntegerField()),
                ('kitongoji', models.CharField(max_length=200)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempMwananchi',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('occupation', models.CharField(max_length=200, null=True)),
                ('kitongoji', models.CharField(max_length=200, null=True)),
                ('mtaa_kijiji', models.CharField(max_length=200, null=True)),
                ('kata', models.CharField(max_length=200, null=True)),
                ('id_card', models.CharField(max_length=20, null=True)),
                ('id_number', models.IntegerField(null=True, unique=True)),
                ('pin', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempVeo',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veo',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('mtaa_kijiji', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('step', models.IntegerField()),
                ('is_active', models.CharField(max_length=20)),
                ('verification_status', models.CharField(max_length=20)),
                ('weo_id', models.CharField(max_length=13, null=True)),
                ('date_weo_verified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weo',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('kata', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=20)),
                ('id_number', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.CharField(max_length=20)),
            ],
        ),
    ]
