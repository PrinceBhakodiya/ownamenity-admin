from django.contrib import admin
from .models import adminModel
# Register your models here.
class showadmin (admin.ModelAdmin):
    list_display = ["admin_name","password","email_id"]

admin.site.register(adminModel,showadmin)
# admin.site.register(adminModel)
# Register your models here.
