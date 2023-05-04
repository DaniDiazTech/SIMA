from django.contrib import admin
from .models import Habit, Daily


class DailyAdmin(admin.ModelAdmin):
    fields = ('habit', 'date', 'is_active')
    list_display = ('habit', 'date', 'is_active')
# Register your models here.
admin.site.register(Habit)
admin.site.register(Daily, DailyAdmin)
