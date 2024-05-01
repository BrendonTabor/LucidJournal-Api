from django.db import models
from .factors import Factors
from .entry import Entry


class DreamFactors(models.Model):
    factor = models.ForeignKey(Factors, on_delete=models.CASCADE)
    dream = models.ForeignKey(Entry, on_delete=models.CASCADE)
    value = models.BooleanField()
