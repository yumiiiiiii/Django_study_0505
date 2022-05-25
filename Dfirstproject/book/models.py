from django.db import models
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag

class M_HashTag(models.Model):
    hashtag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag

class D_HashTag(models.Model):
    hashtag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag


class Romance(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')
    hashtag=models.ManyToManyField(HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="book_photo")

    def __str__(self):
        return self.title

class Mystery(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')
    hashtag=models.ManyToManyField(M_HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="book_photo")

    def __str__(self):
        return self.title

class Disaster(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')
    hashtag=models.ManyToManyField(D_HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="book_photo")

    def __str__(self):
        return self.title

class R_Comment(models.Model):
    post=models.ForeignKey(Romance, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text

class M_Comment(models.Model):
    post=models.ForeignKey(Mystery, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text

class D_Comment(models.Model):
    post=models.ForeignKey(Disaster, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text