from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rules.contrib.views import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy

from lists.models import List


class ListsList(LoginRequiredMixin, ListView):
	model = List
	context_object_name = "lists"
	success_url = reverse_lazy("lists:list")

	def get_queryset(self, *args, **kwargs):
		return List.objects.filter(user=self.request.user)


class ListCreate(LoginRequiredMixin, CreateView):
	model = List
	template_name = "lists/list_create_form.html"
	success_url = reverse_lazy("lists:list")
	fields = ["name"]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class ListUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = List
	template_name = "lists/list_update_form.html"
	success_url = reverse_lazy("lists:list")
	fields = ["name"]
	permission_required = "lists.change_list"


class ListDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = List
	template_name = "lists/list_delete_form.html"
	success_url = reverse_lazy("lists:list")
	permission_required = "lists.change_list"
