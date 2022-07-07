from django.urls import path
from allauth.account.views import LoginView, SignupView

app_name = "gmail"

urlpatterns = [
	# path('', SignupView.as_view(), name="gmail_signup"),
	path('', LoginView.as_view(), name="gmail_login"),
]
