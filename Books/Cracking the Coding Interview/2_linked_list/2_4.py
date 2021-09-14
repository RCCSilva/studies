class Node:
    def __init__(self, value, int):
        self.value = value,
        self.next = next

class LinkedList:
    def __init__(self)
        self.nodes = None
        self.first = None
        self.last = None
        self.size = 0

    def get(index: int) -> Node:
        pass

    def remove(index: int) -> None:
        pass

    def add(node: Node) -> None:
        pass

def parition(linked_list: LinkedList, partitioner: int) -> LinkedList:
    i = 0
    for _ in range(linked_list.length):
        node = linked_list.get(i)
        if node.value >= partitioner:
            linked_list.remove(i)
            linked_list.add(i)
        else:
            i += 1

    return linked_list