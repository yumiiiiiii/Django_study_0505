# Generated by Django 4.0.4 on 2022-05-21 15:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_rename_romance_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='book.mystery')),
            ],
        ),
    ]
