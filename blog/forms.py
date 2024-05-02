from django import forms
from .models import Review,Post

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['user','content','rate']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        #fields='__all__'
        exclude=('user',)