from django.contrib import admin

from tasks.models import Task, List, Status


admin.site.register(Task)
admin.site.register(List)
admin.site.register(Status)

