from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = [ 'title', 'description', 'completed' ]
    list_display = ( 'title', 'description', 'completed' )
    list_filter = [ 'completed' ]
    search_fields = [ 'title' ]
    ordering = [ 'title' ]


admin.site.register(Task, TaskAdmin)
