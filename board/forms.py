from django import forms
from .models import Posting, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'comment_text')
