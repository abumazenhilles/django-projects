from django import forms
from .import models
from .models import Article


class CreateArticle(forms.ModelForm):

    class Meta:
        model = Article
        # fields = ('title', 'slug', 'body', 'thumb')
        fields = '__all__' 
        fields = ['thumb']
