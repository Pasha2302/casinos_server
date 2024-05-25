from django.db import models
from django.utils import timezone


class StateProgram(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    data = models.JSONField()
    start_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "State Program"
        verbose_name_plural = "State Programs"

    def __str__(self):
        return f"{str(self.name).title()} state"
