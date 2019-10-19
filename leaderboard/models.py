import secrets

from django.db import models
from django.contrib.auth.models import User


class Beacon(models.Model):
    def _generate_key():
        return secrets.token_hex(5)

    def _get_default_User():
        return User.objects.filter(is_superuser=True).first()

    key = models.CharField(max_length=10, unique=True, default=_generate_key)
    owner = models.ForeignKey(User, default=_get_default_User,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Touch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
