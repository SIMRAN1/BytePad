from django.conf.urls import url
from views import PaperListAPIView, LastUpdateAPIView, HomeView, SearchView

urlpatterns = [
    url(r'^/api/list/$', PaperListAPIView.as_view(), name='list-papers'),
    url(r'^/api/last-update/$', LastUpdateAPIView.as_view(), name='last-update'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^search/(?P<query>[\w\-]+)/$', SearchView.as_view(), name='search'),
]
