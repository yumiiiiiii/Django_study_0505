from django.contrib import admin
from book.models import Romance, Mystery, Disaster
from .models import Comment, HashTag

# Register your models here.
@admin.register(Romance)
@admin.register(Mystery)
@admin.register(Disaster)

@admin.register(Comment)
@admin.register(HashTag)

class RomanceAdmin(admin.ModelAdmin):
    romance_list=('id','title','author','upload_time','content');

class MysteryAdmin(admin.ModelAdmin):
    mystery_list=('id','title','author','upload_time','content');

class DisasterAdmin(admin.ModelAdmin):
    disaster_list=('id','title','author','upload_time','content');