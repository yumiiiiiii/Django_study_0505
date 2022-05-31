from django.contrib import admin
from main.models import Recipe, Ingredient, Comment, HashTag
from account.models import CustomUser

# Register your models here.
@admin.register(Recipe)
@admin.register(Ingredient)
@admin.register(Comment)
@admin.register(HashTag)
@admin.site.register(CustomUser)

class RecipeAdmin(admin.ModelAdmin):
    posting_list = ('id', 'title', 'content', 'ingredients')