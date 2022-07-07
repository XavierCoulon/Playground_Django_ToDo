from django.urls import path

from tasks.views import TasksView

app_name = "tasks"

urlpatterns = [
	path('list/', TasksView.as_view(), name="list"),
]