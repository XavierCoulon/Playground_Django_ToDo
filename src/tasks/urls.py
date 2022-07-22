from django.urls import path

from tasks.views import TaskCreate, TaskUpdate, TaskDelete, close, reopen, statistics

app_name = "tasks"

urlpatterns = [
	path('create/<int:list>/', TaskCreate.as_view(), name="create"),
	path('update/<int:pk>', TaskUpdate.as_view(), name="update"),
	path('delete/<int:pk>', TaskDelete.as_view(), name="delete"),
	path('close/<int:pk>', close, name="close"),
	path('reopen/<int:pk>', reopen, name="reopen"),
	path('stats/', statistics, name='stats')
]
