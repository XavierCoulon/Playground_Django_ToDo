from django.views.generic import ListView, CreateView, UpdateView
from tasks.models import Task


class TasksList(ListView):
	model = Task
	context_object_name = "tasks"

	def get_queryset(self, *args, **kwargs):
		return Task.objects.filter(list__user=self.request.user).order_by("list")


class TaskCreate(CreateView):
	model = Task
	template_name = "tasks/task_create_form.html"
	fields = "__all__"


class TaskUpdate(UpdateView):
	model = Task
	template_name = "tasks/task_update_form.html"
	fields = "__all__"
