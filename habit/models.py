from datetime import datetime
from pytz import timezone

from django.db import models
from django.contrib.auth import get_user_model

from django.conf.global_settings import LANGUAGE_CODE, TIME_ZONE


User = get_user_model()

# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.user.username + " - " + self.name


class Daily(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    # Auto now add true makes the field uneditable, 
    # making it impossible to change in Django Admin
    date = models.DateField(blank=True)
    is_active = models.BooleanField(default=True) 

    # Date workaround
    def save(self, *args, **kwargs):
        if not self.date:
            utc = datetime.now()
            tz = timezone(TIME_ZONE)
            today = utc.astimezone(tz)
            self.date = today
        super(Daily, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Daily habit"

    def __str__(self):
        return str(self.habit) + " - " + str(self.date)

