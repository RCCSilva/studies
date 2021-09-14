# Create a array where start index is the "n" Stack. So, if Stack 0, will start at the index 0 of the array.
# The Skack 1 at the index 1, and the Stack 2 at the index 2. Each new record at the index should be
# saved at current index plus the maximum amount of Stack.  Thus, given that 3 Stacks will share one
# array, each new record for each Stack should be placed 3 index ahead the current index. If Stack 1 is
# at the index 1, its new record will be stored at index 4, for example.

from typing import List

class MultipleStack:
    def __init__(self, array: List, n: int, max_stacks: int):
        self.array = array
        self.index = n
        self.max_stacks = max_stacks

    def is_empty(self):
        return self.index < self.max_stacks

    def push(self, value):
        self.index += self.max_stacks
        self.array.add(self.index, value)

    def pop(self):
        if self.is_empty:
            raise EmptyStackException()

        value = self.array.get(self.index)
        self.array.add(self.index, None)
        self.index -= self.max_stacks

        return value

    def peek(self):
        if self.is_empty:
            raise EmptyStackException()

        return self.array.get(self.index)

if __name__ == '__main__':
    base_array = []
