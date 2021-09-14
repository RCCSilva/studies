class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user is None:
        raise TypeError('user must not be None')

    if user == '':
        raise ValueError(
            'Empty string is not a valid value for the user paremeter')

    if user in group.get_users():
        return True

    if len(group.get_groups()) == 0:
        return False

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True

    return False


def test():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test 1 - Given user that does exist, return True
    assert is_user_in_group(sub_child_user, parent)

    # Test 2 - Given non existing user, return False
    assert not is_user_in_group('non existing user', parent)

    # Test 3 - Given None value for user, throw Exception
    try:
        is_user_in_group(None, parent)
        assert False
    except TypeError as ex:
        assert str(ex) == 'user must not be None'

    # Test 4 - Given empty string ('') as value for user parameter, throw exception
    try:
        is_user_in_group('', parent)
        assert False
    except ValueError as ex:
        assert str(
            ex) == 'Empty string is not a valid value for the user paremeter'


if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
