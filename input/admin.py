from django.contrib import admin
from django.utils.html import format_html
from .models import batteryDetail

class batteryDetailAdmin(admin.ModelAdmin):

    list_display  = ['no_of_cells', 'voltage', 'c_count', 'mAh']

admin.site.register(batteryDetail, batteryDetailAdmin)