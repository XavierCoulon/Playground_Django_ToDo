from django.views.generic import ListView
from tasks.models import Task


class TasksList(ListView):
	model = Task
	context_object_name = "tasks"

	def get_queryset(self, *args, **kwargs):
		return Task.objects.filter(list__user=self.request.user)
