from django.db import models


class SpecialistOffer(models.Model):
    speciality = models.CharField(max_length=128)
    description = models.TextField(null=True)
    priceperhour = models.FloatField(default=0)
    available_from = models.DateField(null=True)


class CustomerOffer(models.Model):
    speciality = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

