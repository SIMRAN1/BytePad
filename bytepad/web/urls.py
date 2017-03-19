from django.conf.urls import url
from views import PaperListAPIView

urlpatterns = [
    url(r'^list/', PaperListAPIView.as_view(), name='list-papers')
]
