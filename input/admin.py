from django.contrib import admin
from django.utils.html import format_html
from .models import maxCurrent, chargeTime, batteryChoose, continuousCurr

class maxCurrentAdmin(admin.ModelAdmin):
    list_display  = ['capacity', 'c_rating']
admin.site.register(maxCurrent, maxCurrentAdmin)

class chargeTimeAdmin(admin.ModelAdmin):
    list_display  = ['capacity']
admin.site.register(chargeTime, chargeTimeAdmin)

class batteryChooseAdmin(admin.ModelAdmin):
    list_display  = ['voltage', 'current', 'run_time']
admin.site.register(batteryChoose, batteryChooseAdmin)

class continuousCurrAdmin(admin.ModelAdmin):
    list_display  = ['capacity', 'c_rating']
admin.site.register(continuousCurr, continuousCurrAdmin)