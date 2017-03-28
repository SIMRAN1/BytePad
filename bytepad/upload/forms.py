from django import forms

from web.models import Exam, Session, Paper


class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    exam = forms.ModelChoiceField(queryset=Exam.objects.all())
    session = forms.ModelChoiceField(queryset=Session.objects.all())
