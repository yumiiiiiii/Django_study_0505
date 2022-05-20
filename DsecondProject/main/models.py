from django.utils import timezone
from django.db import models
import datetime

# Create your models here.
class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Ingredient(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField('Content')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    hashtags = models.ManyToManyField(HashTag)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text