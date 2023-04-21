from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return f'{instance.id}/{filename}'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    disabled = models.BooleanField(default=False)
    photo = models.ImageField(blank=True, upload_to=upload_to)

    def __str__(self):
        return self.name
