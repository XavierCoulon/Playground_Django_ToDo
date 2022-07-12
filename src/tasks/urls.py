from django.urls import path

from tasks.views import TasksList, TaskCreate, TaskUpdate

app_name = "tasks"

urlpatterns = [
	path('', TasksList.as_view(), name="list"),
	path('create/', TaskCreate.as_view(), name="create"),
	path('update/<int:pk>', TaskUpdate.as_view(), name="update"),
]