from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Can't create database model with it
    class Meta:
        abstract = True

    def __str__(self):
        return self.name
