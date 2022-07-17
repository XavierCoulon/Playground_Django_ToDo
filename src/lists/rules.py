import rules


@rules.predicate
def is_task_owner(user, list):
	return list.user == user


rules.add_perm("lists.change_list", is_task_owner)
rules.add_perm("lists.delete_list", is_task_owner)
