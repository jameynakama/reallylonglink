from django.contrib import admin
from reallylonglink import models


@admin.register(models.ReallyLongLink)
class ReallyLongLinkAdmin(admin.ModelAdmin):
    pass
