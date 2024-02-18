from django.db import models
from datetime import datetime, timedelta


class UserProfile(models.Model):
    uid = models.CharField(max_length=36)
    days_of_use = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.uid

    def save(self, *args, **kwargs):
        if not self.days_of_use:
            self.days_of_use = datetime.now() + timedelta(days=15)
        super(UserProfile, self).save(*args, **kwargs)
