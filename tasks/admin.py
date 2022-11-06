from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = [ 'title', 'description', 'done' ]
    list_display = ( 'title', 'description', 'done' )
    list_filter = [ 'done' ]
    search_fields = [ 'title' ]
    ordering = [ 'title' ]


admin.site.register(Task, TaskAdmin)
