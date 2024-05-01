from django.db import models


class RemCount(models.Model):
    cycles_completed = models.CharField(max_length=255)
