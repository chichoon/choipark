from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=128, required=True)
    content = forms.CharField(required=True)

