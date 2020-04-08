from django.contrib import admin
from .models import UrlMap, UrlProfile
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
admin.site.register(UrlMap)
admin.site.register(UrlProfile)


class UrlMapResource(resources.ModelResource):
    class Meta:
        model = UrlMap


@admin.register(UrlMap)
class documentosAdmin(ImportExportModelAdmin):
    resource_class = UrlMapResource
    list_display = ('user', 'full_url')
    search_fields = ('full_url')
