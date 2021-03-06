# Generated by Django 4.0.4 on 2022-05-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_comment_delete_r_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='romance',
            name='hashtag',
            field=models.ManyToManyField(to='book.hashtag'),
        ),
    ]
