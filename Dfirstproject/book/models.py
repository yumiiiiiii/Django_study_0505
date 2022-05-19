from django.db import models
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag

class Romance(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')
    hashtag=models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

class Mystery(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')

    def __str__(self):
        return self.title

class Disaster(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Romance, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text