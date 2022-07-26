from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from todo.views import index


urlpatterns = [
	path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
	path('', index, name="index"),
	path('accounts/', include('allauth.urls')),
	path('tasks/', include('tasks.urls', namespace="tasks")),
	path('lists/', include('lists.urls', namespace="lists")),
)
