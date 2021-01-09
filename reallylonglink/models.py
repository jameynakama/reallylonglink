import random

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ReallyLongLink(BaseModel):
    original_link = models.URLField(max_length=1000)
    long_link = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.original_link} - {self.long_link[:50]}..."

    def embiggen(self):
        # TODO: Add http to beginning if not given
        long_link = ''
        for i in range(settings.REALLY_LONG_LINK_LENGTH):
            long_link += random.choice(settings.LINK_CHARS)
        self.long_link = long_link
        self.save()


@receiver(pre_save, sender=ReallyLongLink)
def reduce_slashes(sender, **kwargs):
    instance = kwargs['instance']
    if instance.long_link:
        instance.long_link = instance.long_link.replace('//', '/' + random.choice(settings.LINK_CHARS_PLAIN))
        if instance.long_link[0] == '/':
            instance.long_link = random.choice(settings.LINK_CHARS_PLAIN) + instance.long_link[1:]
        if instance.long_link[-1] == '/':
            instance.long_link = instance.long_link[:-1] + random.choice(settings.LINK_CHARS_PLAIN)
