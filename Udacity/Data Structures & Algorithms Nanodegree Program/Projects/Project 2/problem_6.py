class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_list = []
        while cur_head:
            out_list.append(str(cur_head.value))
            cur_head = cur_head.next
        return ' -> '.join(out_list)

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        node = self.head
        result = []
        while node:
            result.append(node.value)
            node = node.next

        return result


def union(llist_1, llist_2):
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())

    r = LinkedList()
    for v in set_1.union(set_2):
        r.append(v)

    return r


def intersection(llist_1, llist_2):
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())

    r = LinkedList()
    for v in set_1.intersection(set_2):
        r.append(v)

    return r


def test():
    # Test 1 - Given two linked of length 3 lists without intersection, return union with 6 values and instersection with 0 values

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = [4, 5, 6]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    union_list_1 = union(linked_list_1, linked_list_2)
    intersection_list_1 = intersection(linked_list_1, linked_list_2)

    assert union_list_1.size() == 6
    assert union_list_1.to_list() == [1, 2, 3, 4, 5, 6]

    assert intersection_list_1.size() == 0
    assert intersection_list_1.to_list() == []

    # Test 2 - Given equal linked list of size 3, return union with 3 values and intersection with 3 values

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_3 = [1, 2, 3]
    element_4 = [3, 2, 1]

    for i in element_3:
        linked_list_3.append(i)

    for i in element_4:
        linked_list_4.append(i)

    union_list_2 = union(linked_list_3, linked_list_4)
    intersection_list_2 = intersection(linked_list_3, linked_list_4)

    assert union_list_2.size() == 3
    assert union_list_2.to_list() == [1, 2, 3]

    assert intersection_list_2.size() == 3
    assert intersection_list_2.to_list() == [1, 2, 3]

    # Test 2 - Given one empty linked list and one of size 3, return union with 3 values and intersection with 0 values

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()  # Empty linked list

    element_5 = [99, 888, 222]

    for i in element_5:
        linked_list_5.append(i)

    union_list_3 = union(linked_list_5, linked_list_6)
    intersection_list_3 = intersection(linked_list_5, linked_list_6)

    assert union_list_3.size() == 3
    assert set(union_list_3.to_list()) == {
        99, 888, 222}, union_list_3.to_list()

    assert intersection_list_3.size() == 0
    assert intersection_list_3.to_list() == []


if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
