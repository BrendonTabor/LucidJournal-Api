from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    date_recorded = models.DateField()
    wake_method = models.ForeignKey("WakeMethod", on_delete=models.CASCADE)
    rem_count = models.ForeignKey("RemCount", on_delete=models.CASCADE)

