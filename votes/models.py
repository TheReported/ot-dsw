from django.conf import settings
from django.db import models

from competitors.models import Competitor


class Vote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vote'
    )
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE, related_name='votes')
    voted_at = models.DateTimeField(auto_now_add=True)
