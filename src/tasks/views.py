from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rules.contrib.views import PermissionRequiredMixin

from tasks.models import Task
from lists.models import List
from tasks.forms import TaskForm


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_create_form.html"

	def form_valid(self, form):
		form.instance.list = List.objects.get(pk=self.kwargs["list"])
		return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_update_form.html"
	permission_required = "tasks.change_task"

	# fields = ["title", "details", "due_date", "favorite", "closed"]


class TaskDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = Task
	permission_required = "tasks.delete_task"

	def get(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("lists:list")


@login_required
def close(request, pk):
	task = Task.objects.get(pk=pk)
	task.close()
	return redirect("lists:list")


@login_required
def reopen(request, pk):
	task = Task.objects.get(pk=pk)
	task.reopen()
	return redirect("lists:list")
