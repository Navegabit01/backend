from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    uid = models.CharField(max_length=36)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    days_of_test = models.PositiveIntegerField(default=15)
    days_of_use_as_premiun = models.PositiveIntegerField(default=30)
    start_date_for_test = models.DateField(auto_now_add=True)
    start_date_for_premiun_use = models.DateField(auto_now_add=True)
    tests_days_selected = models.BooleanField(default=False)
    premiun_days_selected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.uid
