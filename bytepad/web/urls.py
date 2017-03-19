from django.conf.urls import url
from views import PaperListAPIView, LastUpdateAPIView

urlpatterns = [
    url(r'^list/', PaperListAPIView.as_view(), name='list-papers'),
    url(r'^last-update/', LastUpdateAPIView.as_view(), name='last-update')
]
