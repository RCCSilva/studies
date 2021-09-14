class Node:
    def __init__(self, prev, value, min_value):
        self.prev = prev
        self.value = value
        self.min_value = min_value

class StackMin:
    def __init__(self):
        self.top = None

    @property
    def min(self):
        return self.top.min_value

    def pop(self):
        if not self.top:
            raise EmptyStackException()

        value = self.top.value
        self.top = self.top.prev

        return value

    def push(self, value):
        if not self.top:
            self.top = Node(None, value, value)
            return

        min_value = value
        if self.top.value < min_value:
            min_value = self.top.value

        node = Node(self.top, value, min_value)
        self.top = node

    def __str__(self):
        node = self.top
        response = '['
        while node:
            response += str(node.value) + ','
            node = node.prev
        
        return response + ']'


if __name__ == '__main__':
    sm = StackMin()
    sm.push(1)
    print(sm, sm.min)
    sm.push(10)
    print(sm, sm.min)
    sm.push(0)
    print(sm, sm.min)
    sm.pop()
    print(sm, sm.min)
    sm.pop()
    print(sm, sm.min)
