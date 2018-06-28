from django import forms
from .models import Post,ForumSection

class PostCreationForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','section','content']

