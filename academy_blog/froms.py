from django import forms
from .models import Article

field_attrs = {'class': 'form-control'}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['cover_image', 'category', 'title', 'subject']
        widgets = {
            'category': forms.Select(attrs=field_attrs),
            'title': forms.TextInput(attrs=field_attrs),
            'subject': forms.Textarea(attrs=field_attrs),
        }