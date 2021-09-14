def sum_lists(n0: LinkedList, n1: LinkedList) -> Node:
    l0 = n0.last
    l1 = n1.last

    rem = 0

    linked_list = LinkedList()

    while l0 or l1:

        l0_value = l0.value if l0 else 0
        l1_value = l1.value if l1 else 0 

        total = l0_value + l1_value + rem

        linked_list.add(Node(total % 10, None), 0)
        rem = total // 10

        if l0:
            l0 = l0.prev

        if l1:
            l1 = l1.prev

    return linked_list