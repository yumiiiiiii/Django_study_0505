# Generated by Django 4.0.4 on 2022-05-03 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='upload_time',
        ),
    ]
