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
            'content',
            'ingredients',
            #'hashtags',
            'photo',
        ]
    #hashtags = forms.CharField(label="해시태그", max_length=200, widget=forms.TextInput(attrs={'size':'40'}))
    ingredients = CustomIngrdntForm(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple)

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = "__all__"
        exclude = ('recipe',)