from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import UserAccount
# Register your models here.

@admin.register(UserAccount)
class PostAdmin(admin.ModelAdmin):
    list_display = ('account','username', 'verified', 'is_staff')
    search_fields = ('account','username', )