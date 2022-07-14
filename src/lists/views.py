from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from lists.models import List


class ListsList(ListView):
	model = List
	context_object_name = "lists"

	def get_queryset(self, *args, **kwargs):
		return List.objects.filter(user=self.request.user)


class ListCreate(CreateView):
	model = List
	template_name = "lists/list_create_form.html"
	fields = ["name"]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class ListUpdate(UpdateView):
	model = List
	template_name = "lists/list_update_form.html"
	fields = ["name"]


class ListDelete(DeleteView):
	model = List
	template_name = "lists/list_delete_form.html"

	def get_success_url(self):
		return reverse("lists:list")
