from django.db import models
from django.forms.fields import ImageField
from django.utils.safestring import mark_safe

class batteryDetail(models.Model):
    no_of_cells = models.PositiveIntegerField()
    voltage = models.FloatField()
    c_count = models.PositiveIntegerField()
    mAh = models.PositiveBigIntegerField()
    def __str__(self):
        return str(self.no_of_cells)