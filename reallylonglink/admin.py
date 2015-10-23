from django.contrib import admin
from reallylonglink.models import ReallyLongLink


class ReallyLongLinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(ReallyLongLink)