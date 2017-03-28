from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        Paper = self.get_model('Paper')
        watson.register(Paper)
