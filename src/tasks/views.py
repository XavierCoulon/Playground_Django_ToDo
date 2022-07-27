import json

from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rules.contrib.views import PermissionRequiredMixin, objectgetter
from rules.contrib.views import permission_required
from django.db.models import Count, Q
from django.shortcuts import render
from django.utils.translation import gettext

from tasks.models import Task
from lists.models import List
from tasks.forms import TaskForm


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_create_form.html"
	success_url = reverse_lazy("lists:list")

	def form_valid(self, form):
		form.instance.list = List.objects.get(pk=self.kwargs["list"])
		return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = Task
	form_class = TaskForm
	template_name = "tasks/task_update_form.html"
	permission_required = "tasks.change_task"
	success_url = reverse_lazy("lists:list")


class TaskDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = Task
	permission_required = "tasks.delete_task"
	success_url = reverse_lazy("lists:list")
	template_name = "lists/list_list.html"


@login_required()
@permission_required("tasks.change_task", fn=objectgetter(Task, "pk"), raise_exception=True)
def close(request, pk):
	Task.objects.get(pk=pk).close()
	return redirect("lists:list")


@login_required
@permission_required("tasks.change_task", fn=objectgetter(Task, "pk"), raise_exception=True)
def reopen(request, pk):
	Task.objects.get(pk=pk).reopen()
	return redirect("lists:list")


@login_required
def statistics(request):
	dataset = Task.objects.filter(list__user=request.user).values("list__name").annotate(
		closed_count=Count("list", filter=Q(closed=True)),
		not_closed_count=Count("list", filter=Q(closed=False))
	)

	lists = closed_series_data = not_closed_series_data = []

	for entry in dataset:
		lists.append(entry['list__name'])
		closed_series_data.append(entry['closed_count'])
		not_closed_series_data.append(entry['not_closed_count'])

	closed_series = {
		'name': gettext('Fermées'),
		'data': closed_series_data,
		'color': 'green'
	}

	not_closed_series = {
		'name': gettext('Ouvertes'),
		'data': not_closed_series_data,
		'color': 'blue'
	}

	chart = {
		'chart': {'type': 'column'},
		'title': {'text': gettext('Tâches par statut')},
		'xAxis': {'categories': lists},
		'series': [closed_series, not_closed_series]
	}

	dump = json.dumps(chart)

	return render(request, 'tasks/statistics.html', {'chart': dump})
