# Generated by Django 4.0.4 on 2022-05-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_rename_comment_r_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_photo'),
        ),
        migrations.AddField(
            model_name='mystery',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_photo'),
        ),
    ]