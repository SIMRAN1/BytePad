from django.conf.urls import url

from views import LoginView, UploadView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', UploadView.as_view(), name='upload'),
    # url(r'^login/$', LoginView.as_view(), name='login'),
]
