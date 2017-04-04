from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Subject Name'}))
