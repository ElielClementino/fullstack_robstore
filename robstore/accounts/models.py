from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    avatar = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_stored = models.DecimalField(default=0.00, decimal_places=2, max_digits=12)
