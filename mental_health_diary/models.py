from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Entry(models.Model):
    user = models.ManyToManyField(User)
    happiness = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    disgust = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    url = models.CharField(null=True, max_length=10)

    class Meta:
        verbose_name_plural = "Entries"