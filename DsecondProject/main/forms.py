from django import forms
from .models import Recipe, Ingredient

class CustomIngrdntForm(forms.ModelMultipleChoiceField):
    def label_from_instance(self, Ingredient):
        return "%s" %Ingredient.name

class Form(forms.ModelForm):
    class Meta:
        model = Recipe
        
        fields = [
            'title',
            'upload_time',
            'ingredients',
            'content'
        ]

    title = forms.CharField()
    upload_time = forms.DateInput()
    ingredients = CustomIngrdntForm(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple)