from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from web.models import Paper, LastUpdate

from forms import UploadForm


class LoginView(FormView):
    template_name = 'login.html'
    success_url = '/admin/'
    form_class = AuthenticationForm

    def get(self, request):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(self.success_url)
        return super(LoginView, self).get(request)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


class UploadView(LoginRequiredMixin, FormView):
    login_url = '/admin/login/'
    redirect_field_name = 'next'
    template_name = 'upload.html'
    success_url = '/'
    form_class = UploadForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def form_valid(self, form):
        files = self.request.FILES.getlist('file')
        exam = form.cleaned_data['exam']
        session = form.cleaned_data['session']
        papers = []
        for f in files:
            # Do something with each file.
            papers.append(Paper(name=f.name, file=f, exam=exam, session=session))
        Paper.objects.bulk_create(papers)

        return HttpResponseRedirect(self.get_success_url())
