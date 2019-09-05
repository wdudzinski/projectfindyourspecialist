from django.db import models
from django.contrib.auth.models import User


class SpecialistOffer(models.Model):
    speciality = models.CharField(max_length=128)
    description = models.TextField(null=True)
    priceperhour = models.FloatField(default=0)
    available_from = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CustomerOffer(models.Model):
    speciality = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

