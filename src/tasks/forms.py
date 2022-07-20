from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ["title", "details", "due_date", "favorite"]

		widgets = {
			'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'placeholder': 'Select a date', 'type': 'date'})
		}
