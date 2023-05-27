from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.
class Goal(models.Model):

    deadline = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    name = models.CharField(_(""), max_length=300)
    relevance = models.CharField(_(""), choices = [(1, "Intensa"), (2, "Tranquila"), (3, "Relax")], default="Tranquila", max_length=12) 
    urgency = models.CharField(_(""), choices=[(1, "Alta"), (2, "Media"), (3, "Baja")], default="Media", max_length=12)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Goal_detail", kwargs={"pk": self.pk})

class Task(models.Model):
    name = models.CharField(_(""), max_length=300)
    done = models.BooleanField(_("")) 
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    parent_goal = models.ForeignKey(Goal, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})

