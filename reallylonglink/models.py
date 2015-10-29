import random

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ReallyLongLink(BaseModel):
    original_link = models.URLField(max_length=1000)
    long_link = models.CharField(max_length=2000)

    def __str__(self):
        return "{} - {}...".format(self.original_link, self.long_link[:50])

    def embiggen(self):
        # TODO: Add http to beginning if not given
        long_link = ''
        for i in range(settings.REALLY_LONG_LINK_LENGTH):
            long_link += random.choice(settings.LINK_CHARS)
        self.long_link = long_link
        self.save()
