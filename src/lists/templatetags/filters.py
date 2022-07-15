from django import template
from tasks.models import Task

register = template.Library()


# Not used anymore
@register.filter(name="has_tasks_closed")
def has_tasks_closed(list):
    return Task.objects.filter(list=list, closed=True)
