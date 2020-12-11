from django.contrib import admin
from .models import KeywordModel
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class KeywordAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(KeywordModel,KeywordAdmin)

# Register your models here.
