from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from plagiatLocal.models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin):
    pass