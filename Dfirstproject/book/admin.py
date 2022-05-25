from django.contrib import admin
from book.models import Romance, Mystery, Disaster
from .models import *

# Register your models here.
@admin.register(Romance)
@admin.register(Mystery)
@admin.register(Disaster)

@admin.register(R_Comment)
@admin.register(HashTag)
@admin.register(M_Comment)
@admin.register(M_HashTag)
@admin.register(D_Comment)
@admin.register(D_HashTag)



class RomanceAdmin(admin.ModelAdmin):
    romance_list=('id','title','author','upload_time','content');

class MysteryAdmin(admin.ModelAdmin):
    mystery_list=('id','title','author','upload_time','content');

class DisasterAdmin(admin.ModelAdmin):
    disaster_list=('id','title','author','upload_time','content');