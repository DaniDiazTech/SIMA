from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from utils.models import BaseModel

User = get_user_model()

class Account(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE) # Deletes profile if user is deleted
    occupation = models.CharField(_("Occupation"), max_length=140, blank=True, null=True)
    birthday = models.DateField(_("Birthday"), auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"pk": self.pk})
