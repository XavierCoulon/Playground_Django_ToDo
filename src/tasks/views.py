from django.views.generic import ListView
from tasks.models import Task


class TasksView(ListView):
	model = Task
	context_object_name = "tasks"
