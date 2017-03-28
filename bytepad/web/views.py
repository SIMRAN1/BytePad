from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from watson import search as watson

from forms import SearchForm
from models import Paper, LastUpdate
from serializers import PaperSerilaizer


class HomeView(TemplateView):
    """
    Landing page of the website
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search', query=form.data['name'])


class SearchView(TemplateView):
    """
    Search results page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['form'] = SearchForm(initial={'name': context.get('query')})
        results = watson.filter(Paper, context.get('query'))
        context['queryset'] = results
        return context

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search', query=form.data['name'])


class PaperListAPIView(ListAPIView):
    """
    Lists all the papers available for download
    """
    queryset = Paper.objects.all()
    serializer_class = PaperSerilaizer


class LastUpdateAPIView(APIView):
    """
    Last update timestamp
    """

    def get(self, request, *args, **kwargs):
        last_update = str(LastUpdate.objects.order_by('timestamp').first())
        return Response({'timestamp': last_update})
