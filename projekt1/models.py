from django.db import models


class SpecialistOffer(models.Model):
    name = models.CharField(max_length=128)
    speciality = models.CharField(max_length=128)
    description = models.TextField()
    priceperhour = models.FloatField(default=0)
    available_from = models.DateField(null=True)
    available_to = models.DateField(null=True)


class CustomerOffer(models.Model):
    name = models.CharField(max_length=128)
    speciality = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

