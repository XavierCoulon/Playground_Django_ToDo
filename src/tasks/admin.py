from django.contrib import admin

from tasks.models import Task, List


admin.site.register(List)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

	list_display = ["title", "list", "closed", "details"]

	def get_form(self, request, obj=None, **kwargs):
		form = super(TaskAdmin, self).get_form(request, obj, **kwargs)
		form.base_fields["closed"].initial = False
		return form



