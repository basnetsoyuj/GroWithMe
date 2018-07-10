from django import forms
from .models import Post,ForumSection

class PostCreationForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','section','subject','content']

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        self.fields['section'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'