from django import forms

from web.models import Exam, Session, Paper


class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    exam = forms.ModelChoiceField(queryset=Exam.objects.all())
    session = forms.ModelChoiceField(queryset=Session.objects.all())

    # def save(self):
    #     exam = self.cleaned_data['exam']
    #     session = self.cleaned_data['session']
    #     papers = []
    #     for paper in self.files:
    #         papers.append(Paper(name='', file='', exam=exam, session=session))
    #     Paper.objects.bulk_create(papers)
