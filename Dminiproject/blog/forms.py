from django import forms
from .models import Blog
from dataclasses import field
from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['country', 'plate_name', 'title',
                  'minutes', 'upload_time', 'content', 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']
