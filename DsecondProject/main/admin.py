from django.contrib import admin
from main.models import Recipe, Ingredient, Comment, HashTag

# Register your models here.
@admin.register(Recipe)
@admin.register(Ingredient)
@admin.register(Comment)
@admin.register(HashTag)

class RecipeAdmin(admin.ModelAdmin):
    posting_list = ('id', 'title', 'content', 'ingredients')