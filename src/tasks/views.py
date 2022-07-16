from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rules.contrib.views import PermissionRequiredMixin

from tasks.models import Task
from lists.models import List
from tasks.forms import TaskForm


class TasksList(LoginRequiredMixin, ListView):
	model = Task
	context_object_name = "tasks"

	def get_queryset(self, *args, **kwargs):
		return Task.objects.filter(list__user=self.request.user).order_by("list")


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_create_form.html"

	def form_valid(self, form):
		form.instance.list = List.objects.get(pk=self.kwargs["list"])
		return super().form_valid(form)


class TaskUpdate(PermissionRequiredMixin, UpdateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_update_form.html"
	permission_required = "tasks.change_task"

	# fields = ["title", "details", "due_date", "favorite", "closed"]


class TaskDelete(LoginRequiredMixin, DeleteView):
	model = Task

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
def unclose(request, pk):
	task = Task.objects.get(pk=pk)
	task.reopen()
	return redirect("lists:list")
