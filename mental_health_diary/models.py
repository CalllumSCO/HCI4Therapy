from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


# Create your models here.


class ActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.type

class Activity(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    activity = models.CharField(max_length=64)
    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, null=True, unique=False)
    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = "Activities"

class ActivityEntry(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1440)])
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, unique=False)
    date = models.DateField(default=date.today())
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.CharField(null=True, max_length=10)



    class Meta:
        verbose_name_plural = "Activity Entries"

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today())
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    happiness = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    anger = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    disgust = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    fear = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    power = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    peace = models.IntegerField(default=0, validators=[MinValueValidator(-5), MaxValueValidator(5)])
    mood = models.FloatField(default=0)
    best_moment = models.TextField(max_length=500, default='')
    share_best = models.TextField(max_length=500, default='')
    worst_moment = models.TextField(max_length=500, default='')
    deal_worst = models.TextField(max_length=500, default='')
    coping_mech = models.TextField(max_length=500, default='')
    anything_different = models.TextField(max_length=500, default='')
    smile = models.TextField(max_length=500, default='')
    url = models.CharField(null=True, max_length=10)
    class Meta:
        verbose_name_plural = "Entries"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=32, null=True)
    url = models.URLField()

    def __str__(self):
        return self.title

