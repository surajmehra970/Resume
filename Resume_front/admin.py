from django.contrib import admin
from .models import msgreq

@admin.register(msgreq)
class msgAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'subject')