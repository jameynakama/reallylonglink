from django.db import models


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ReallyLongLink(BaseModel):
    original_link = models.CharField(max_length=2000)
    long_link = models.CharField(max_length=2000)
