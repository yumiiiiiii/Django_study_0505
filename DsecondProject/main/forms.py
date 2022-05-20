from django import forms
from .models import Recipe, Ingredient, Comment

class CustomIngrdntForm(forms.ModelMultipleChoiceField):
    def label_from_instance(self, Ingredient):
        return "%s" %Ingredient.name

class Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'content'
        ]

    ingredients = CustomIngrdntForm(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple)

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = "__all__"
        exclude = ('recipe',)