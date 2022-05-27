from django.db import models
from turtle import title
from django.utils import timezone

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=50, blank=True)
    upload_time = models.DateTimeField('date published')
    body = models.TextField(null = True, default = "")
    
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    
class Comment(models.Model):
    post = models.ForeignKey(Posting, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def approve(self):
        self.save
        
    def __str__(self):
        return self.comment_text
    
class HashTag(models.Model):
    hashtag = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.hashtag