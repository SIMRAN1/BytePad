from rest_framework import serializers
from models import Paper


class PaperSerilaizer(serializers.ModelSerializer):
    exam = serializers.CharField()
    session = serializers.CharField()

    def get_exam(self):
        return self.exam.name

    def get_session(self):
        return self.session.year

    class Meta:
        model = Paper
        fields = ('name', 'file', 'exam', 'session')
