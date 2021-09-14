class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def kth_element(node: Node, index: int):
    if index < 0:
        return None

    i = 0
    while node and i < index:
        node = node.next
        i += 1

    if not node:
        return None

    return node.value

if __name__ == '__main__':
    print(kth_element(Node(1, Node(2, Node(3, None))), -1))