from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100)
