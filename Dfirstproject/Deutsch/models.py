from django.db import models
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Posting(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content = models.TextField('Content')
    hashtag = models.ManyToManyField(HashTag)
    photo = models.ImageField(blank=True,null=True,upload_to="post_photo")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Posting, related_name='comments',on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text