from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import batteryDetail

class batteryDetailForm(ModelForm):
    class Meta:
        model = batteryDetail
        fields = '__all__'