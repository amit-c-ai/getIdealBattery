from django.db import models
from django.forms.fields import ImageField
from django.utils.safestring import mark_safe

class maxCurrent(models.Model):
    capacity = models.PositiveBigIntegerField()
    c_rating = models.FloatField()

class chargeTime(models.Model):
    capacity = models.PositiveBigIntegerField()

class batteryChoose(models.Model):
    voltage = models.FloatField()
    current = models.PositiveBigIntegerField()
    run_time = models.PositiveBigIntegerField()

class continuousCurr(models.Model):
    capacity = models.PositiveBigIntegerField()
    c_rating = models.FloatField()
