from rest_framework.serializers import ModelSerializer
from models import Paper


class PaperSerilaizer(ModelSerializer):
    class Meta:
        model = Paper
        fields = ('name', 'file', 'exam', 'session')
