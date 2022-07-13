from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from tasks.models import Task
from lists.models import List
from tasks.forms import TaskForm


class TasksList(ListView):
	model = Task
	context_object_name = "tasks"

	def get_queryset(self, *args, **kwargs):
		return Task.objects.filter(list__user=self.request.user).order_by("list")


class TaskCreate(CreateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_create_form.html"

	def form_valid(self, form):
		form.instance.list = List.objects.get(pk=self.kwargs["list"])
		return super().form_valid(form)


class TaskUpdate(UpdateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_update_form.html"
	# fields = ["title", "details", "due_date", "favorite", "closed"]


class TaskDelete(DeleteView):
	model = Task

	def get(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("tasks:list")


def close(request, pk):
	task = Task.objects.get(pk=pk)
	task.close()
	return redirect("tasks:list")


def unclose(request, pk):
	task = Task.objects.get(pk=pk)
	task.unclose()
	return redirect("tasks:list")
