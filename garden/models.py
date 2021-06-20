from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from localflavor.us.models import USPostalCodeField


class Profile(models.Model):
    PIEDMONT = 'PM'
    MOUNTAINS = 'MT'
    COASTAL_PLAIN = 'CP'

    REGION_CHOICES = [
        (PIEDMONT, 'Piedmont'),
        (MOUNTAINS, 'Mountains'),
        (COASTAL_PLAIN, 'Coastal Plain'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = USPostalCodeField()
    experience_level = models.IntegerField()
    name = models.CharField(max_length=240)
    effort_level = models.IntegerField()
    region = models.CharField(choices=REGION_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Plant(models.Model):
    common_name = models.CharField(max_length=240, blank=True, null=True)
    scientific_name = models.CharField(max_length=240, blank=True, null=True)
    zones = models.ManyToManyField('GrowingZone', related_name="plants")

    def __str__(self):
        return self.common_name if self.common_name else self.scientific_name


class GrowingZone(models.Model):
    usda_zone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.usda_zone


class GrowingSchedule(models.Model):
    text = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules")
    plant = models.ManyToManyField('Plant', related_name="schedules")

    def __str__(self):
        return self.text


class LightNeeded(models.Model):
    shade = models.CharField(max_length=280)

    def __str__(self):
        return self.shade


