from django.contrib import admin
from .models import FileUploader
# Register your models here.
# admin.site.register(FileUploader)

@admin.register(FileUploader)
class FileUploaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    search_fields = ('name',)
    list_filter = ('name',)