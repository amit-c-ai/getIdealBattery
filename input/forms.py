from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import maxCurrent, chargeTime, batteryChoose

class maxCurrentForm(ModelForm):
    class Meta:
        model = maxCurrent
        fields = '__all__'

class chargeTimeForm(ModelForm):
    class Meta:
        model = chargeTime
        fields = '__all__'

class batteryChooseForm(ModelForm):
    class Meta:
        model = batteryChoose
        fields = '__all__'