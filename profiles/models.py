import os

from django.db import models
from django.contrib.auth.models import AbstractUser, User
# from django.core.validators import RegexValidator # To use later in a phone number validation
from django.conf import settings

# Create your models here.


class Address(models.Model):
    province = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    neighbor = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    street_number = models.IntegerField(blank=True, null=True)
    manzana = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.street + ' ' + self.street_number


def get_image_path(instance, filename):
    """build the upload path for the image"""
    instance_id = instance.id
    if instance_id is None:
        instance_id = Person.objects.order_by("id").last().id + 1
    path = os.path.join("images/users/", str(instance_id), "profile", filename)
    return path


class Person(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.ForeignKey(Address, related_name='people', on_delete=models.PROTECT, null=True, blank=True)
    picture = models.ImageField(upload_to=get_image_path, null=True, blank=True)
