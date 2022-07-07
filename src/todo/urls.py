from django.contrib import admin
from django.urls import path, include
from todo.views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('authentification.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('gmail.urls')),
    path('tasks/', include('tasks.urls')),
]
