from django import forms
from furniture_main.models import Article as Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'image']