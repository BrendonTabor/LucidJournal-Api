from django.db import models


class SleepFactor(models.Model):
    label = models.CharField(max_length=255)
