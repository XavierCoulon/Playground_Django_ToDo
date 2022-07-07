from django.contrib.auth.forms import UserCreationForm
from authentification.models import CustomUser


class SignUpForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ("email",)

