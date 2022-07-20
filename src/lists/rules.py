import rules


@rules.predicate
def is_list_owner(user, list):
	return list.user == user


rules.add_perm("lists.change_list", is_list_owner)
rules.add_perm("lists.delete_list", is_list_owner)
