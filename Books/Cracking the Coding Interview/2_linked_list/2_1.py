class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        x = self
        start = '['
        while x:
            start += str(x.value) + ','
            x = x.next
        return start + ']'

# 1. Time: O(n). Memory: o(n)

def remove_duplicates(node: Node) -> Node:
    first = p0 = p1 = node
    history = {first.value}

    while p0.next:
        if p0.next.value in history:
            p0.next = p0.next.next
        else:
            history.add(p0.value)
            p0 = p0.next

    return first

# 2. Time: O(n²). Memory: O(1)

def remove_duplicates(node: Node) -> Node:
    first = p0 = p1 = node

    while p0.next:
        while p1.next:
            if p0.value == p1.next.value:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        p0 = p0.next

    return first

if __name__ == '__main__':
    test = Node(2, Node(1, Node(2, None)))
    print(remove_duplicates(test))