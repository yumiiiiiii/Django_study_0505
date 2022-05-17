from django.db import models
import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField('Content')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    
    def __str__(self):
        return self.title
