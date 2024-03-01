# models.py

from django.db import models
from django.conf import settings

class DetectionResult(models.Model):
    image = models.ImageField(upload_to='photos/')   
    maladie = models.CharField(max_length=255)

    def image_url(self):
        return f"{settings.MEDIA_URL}{self.image}"

    def __str__(self):
        return f"{self.image}"