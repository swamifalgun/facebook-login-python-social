from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=255, null=True, blank=True, default=None, db_index=True,
                              help_text=u'Email address used for login into facebook')
    token = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name