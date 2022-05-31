from xml.etree.ElementTree import Comment
from django.contrib import admin
from Deutsch.models import Posting, Comment, HashTag
# Register your models here.
@admin.register(Posting)
@admin.register(Comment)
@admin.register(HashTag)

class PostingAdmin(admin.ModelAdmin):
    posting_list = ('id','title','upload_time','content');