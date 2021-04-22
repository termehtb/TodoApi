from django.contrib import admin

# Register your models here.
from jobs.models import Todojob



@admin.register(Todojob)
class TodoAdmin(admin.ModelAdmin):
    pass
