from django.db import models


class WakeMethod(models.Model):
    label = models.CharField(max_length=255)
