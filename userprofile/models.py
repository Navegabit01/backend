from django.db import models
from datetime import datetime, timedelta


class UserProfile(models.Model):
    uid = models.CharField(max_length=64)
    days_of_use = models.DateField(default=datetime.now()+timedelta(days=30))
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.uid
