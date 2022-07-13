from django.urls import path

from tasks.views import TasksList, TaskCreate, TaskUpdate, TaskDelete, close, unclose

app_name = "tasks"

urlpatterns = [
	path('', TasksList.as_view(), name="list"),
	path('create/<int:list>/', TaskCreate.as_view(), name="create"),
	path('update/<int:pk>', TaskUpdate.as_view(), name="update"),
	path('delete/<int:pk>', TaskDelete.as_view(), name="delete"),
	path('close/<int:pk>', close, name="close"),
	path('unclose/<int:pk>', unclose, name="unclose"),
]