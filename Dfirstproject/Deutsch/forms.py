from dataclasses import field
from pyexpat import model
from django import forms
from .models import Posting, Comment

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title','content','photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']