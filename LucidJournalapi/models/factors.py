from django.db import models


class Factors(models.Model):
    label = models.CharField(max_length=255)
