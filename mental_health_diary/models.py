from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    happiness = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    disgust = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    url = models.CharField(null=True, max_length=10)

    class Meta:
        verbose_name_plural = "Entries"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=32, null=True)
    description = models.TextField(max_length=256)
    url = models.URLField()

    def __str__(self):
        return self.title