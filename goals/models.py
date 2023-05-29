from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from utils.models import BaseModel

User = get_user_model()

class Goal(BaseModel):

    class UrgencyChoices(models.TextChoices):
        HIGH = "HI", _("High")
        MEDIUM = "MD", _("Medium")
        LOW = "LOW", _("Low")

    class RelevanceChoices(models.TextChoices):
        HIGH = "HI", _("High")
        MEDIUM = "MD", _("Medium")
        LOW = "LOW", _("Low")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(_("Deadline"), auto_now=False, auto_now_add=False)
    name = models.CharField(_("Name"), max_length=300)
    relevance = models.CharField(_("Relevance"), choices = RelevanceChoices.choices, default=RelevanceChoices.MEDIUM, max_length=12) 
    urgency = models.CharField(_("Urgency"), choices=UrgencyChoices.choices, default = UrgencyChoices.MEDIUM, max_length=12)
    
    class Meta:
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Goal_detail", kwargs={"pk": self.pk})

class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(_("Task name"), max_length=300)
    done = models.BooleanField(_("Done?")) 
    
    parent_goal = models.ForeignKey(Goal, verbose_name=_("Linked Goal"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})

