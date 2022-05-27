from django.contrib import admin
from board.models import Posting, Comment, HashTag
# Register your models here.
@admin.register(Posting)
@admin.register(Comment)
@admin.register(HashTag)

class PostingAdmin(admin.ModelAdmin):
    posting_list = ('id', 'title', 'upload_time', 'summary');
    