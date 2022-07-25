import rules


@rules.predicate
def is_task_owner(user, task):
	print(user)
	print(task.list.user)
	return task.list.user == user


rules.add_perm("tasks.change_task", is_task_owner)
rules.add_perm("tasks.delete_task", is_task_owner)
