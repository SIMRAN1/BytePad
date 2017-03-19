from rest_framework.generics import ListAPIView
from models import Paper
from serializers import  PaperSerilaizer


class PaperListAPIView(ListAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerilaizer
