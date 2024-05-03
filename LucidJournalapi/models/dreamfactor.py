from django.db import models
from .sleepfactor import SleepFactor
from .entry import Entry


class DreamFactor(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    sleepfactor = models.ForeignKey(SleepFactor, on_delete=models.CASCADE)
