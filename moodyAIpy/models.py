import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Project uses Django's User object model

class AIResponse(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  prompt = models.CharField(max_length=400)
  response = models.CharField(max_length=400)
  mood = models.CharField(max_length=100)
  favorite = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.prompt

  def is_recent(self):
    return self.timestamp >= timezone.now() - datetime.timedelta(days=1)