from django.contrib import admin
from main.models import Recipe, Ingredient

# Register your models here.
@admin.register(Recipe)
@admin.register(Ingredient)

class RecipeAdmin(admin.ModelAdmin):
    posting_list = ('id', 'title', 'content', 'ingredients')