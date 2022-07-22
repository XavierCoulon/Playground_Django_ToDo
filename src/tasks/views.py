import json

from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from rules.contrib.views import PermissionRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import render

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
	success_url = reverse_lazy("lists:list")
	template_name = "lists/list_list.html"


	# def get(self, request, *args, **kwargs):
	# 	return self.delete(request, *args, **kwargs)

	# def get_success_url(self):
	# 	return reverse("lists:list")


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


@login_required
def statistics(request):
	dataset = Task.objects.filter(list__user=request.user).values("list__name").annotate(
		closed_count=Count("list", filter=Q(closed=True)),
		not_closed_count=Count("list", filter=Q(closed=False))
	)

	lists = list()
	closed_series_data = list()
	not_closed_series_data = list()

	for entry in dataset:
		lists.append(entry['list__name'])
		closed_series_data.append(entry['closed_count'])
		not_closed_series_data.append(entry['not_closed_count'])

	closed_series = {
		'name': 'Fermées',
		'data': closed_series_data,
		'color': 'green'
	}

	not_closed_series = {
		'name': 'Ouvertes',
		'data': not_closed_series_data,
		'color': 'blue'
	}

	chart = {
		'chart': {'type': 'column'},
		'title': {'text': 'Tâches par statut'},
		'xAxis': {'categories': lists},
		'series': [closed_series, not_closed_series]
	}

	dump = json.dumps(chart)

	return render(request, 'tasks/statistics.html', {'chart': dump})
