from dataclasses import field
from django import forms
from .models import *

class R_Form(forms.ModelForm):
    class Meta:
        model=Romance
        fields=['title','content','author','photo']

class M_Form(forms.ModelForm):
    class Meta:
        model=Mystery
        fields=['title','content','author','photo']

class D_Form(forms.ModelForm):
    class Meta:
        model=Disaster
        fields=['title','content','author','photo']

class R_CommentForm(forms.ModelForm):
    class Meta:
        model=R_Comment
        fields=['username','comment_text']

class M_CommentForm(forms.ModelForm):
    class Meta:
        model=M_Comment
        fields=['username','comment_text']

class D_CommentForm(forms.ModelForm):
    class Meta:
        model=D_Comment
        fields=['username','comment_text']

