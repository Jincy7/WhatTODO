import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.

class TODO(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )
    todo_id = models.AutoField(primary_key=True)
    todo_title = models.CharField(max_length=200)
    todo_contents = models.TextField(blank=True)
    todo_expire_date = models.DateTimeField('Expire date', default=datetime.datetime.now)
    todo_is_prior = models.BooleanField(default=False)
    todo_has_expire_date = models.BooleanField(default=False)
    todo_is_finished = models.BooleanField(default=False)

    def is_expired_todo(self):
        return self.todo_expire_date < timezone.now()
