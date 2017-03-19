from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from models import Paper, LastUpdate
from serializers import PaperSerilaizer


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
