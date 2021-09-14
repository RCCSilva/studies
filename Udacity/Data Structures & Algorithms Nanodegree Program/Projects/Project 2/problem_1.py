class Value:
    def __init__(self, value, usage_node):
        self.value = value
        self.usage_node = usage_node


class UsageNode:
    def __init__(self, count):
        self.use_count = count
        self._data = set()
        self.next = None
        self.last = None

    def add(self, key):
        self._data.add(key)

    def remove(self, key):
        self._data.remove(key)

    def pop(self):
        return self._data.pop()

    @property
    def size(self):
        return len(self._data)

    def __repr__(self):
        values = [
            f'<UsageNode use_count={self.use_count} keys="{self._data}">']

        node = self.next

        while node:
            values.append(
                f'<UsageNode use_count={node.use_count} keys="{node._data}">')
            node = node.next

        return ' -> '.join(values)


class LRU_Cache:

    def __init__(self, capacity):
        if capacity is None:
            raise TypeError('capacity must not be None')

        if capacity <= 0:
            raise ValueError('capacity must be a positive integer')

        self.capacity = capacity
        self._data = {}
        self._head_usage_node = None

    def get(self, key):
        if key not in self._data:
            return -1

        v = self._data[key]

        v.usage_node = self.__update_node_count(key, v.usage_node)

        return v.value

    def set(self, key, value):
        if key is None:
            raise TypeError('"key" parameter must not be None')

        if len(self._data) == self.capacity:
            self.__free_space()

        if self._head_usage_node is None or self._head_usage_node.use_count != 1:
            usage_node = UsageNode(1)

            if self._head_usage_node is not None:
                usage_node.next = self._head_usage_node

            self._head_usage_node = usage_node

        else:
            usage_node = self._head_usage_node

        usage_node.add(key)

        self._data[key] = Value(value, usage_node)

    def __update_node_count(self, key, usage_node: UsageNode) -> UsageNode:
        new_use_count = usage_node.use_count + 1

        usage_node.remove(key)

        if usage_node.next and usage_node.next.use_count == new_use_count:
            new_usage_node = usage_node.next
            new_usage_node.add(key)
        else:
            new_usage_node = UsageNode(new_use_count)
            new_usage_node.add(key)

            if usage_node.next is not None:
                new_usage_node.next = usage_node.next
                usage_node.next.last = new_usage_node

            new_usage_node.last = usage_node
            usage_node.next = new_usage_node

        if usage_node.size == 0:
            if usage_node.last is not None:
                new_usage_node.last = usage_node.last
                usage_node.last.next = new_usage_node
            else:
                self._head_usage_node = new_usage_node

        return new_usage_node

    def __free_space(self):
        key = self._head_usage_node.pop()
        if self._head_usage_node.size == 0:
            self._head_usage_node = self._head_usage_node.next
            self._head_usage_node.last = None

        del self._data[key]


def test():
    # Test 1 - Given LRU with capacity 5, assert least used data (3) is deleted when loading more data than its capacity
    test_cache_1 = LRU_Cache(5)

    test_cache_1.set(1, 1)
    test_cache_1.set(2, 2)
    test_cache_1.set(3, 3)
    test_cache_1.set(4, 4)

    assert test_cache_1.get(1) == 1
    assert test_cache_1.get(2) == 2
    assert test_cache_1.get(9) == -1

    test_cache_1.set(5, 5)
    test_cache_1.set(6, 6)

    assert test_cache_1.get(3) == -1

    test_cache_1.set(7, 7)

    assert test_cache_1.get(4) == -1

    # Test 2 - Given LRU with capacity 2, when LRU is fully loaded and the data was used at least two times, set a new value without exceptions
    test_cache_2 = LRU_Cache(2)
    test_cache_2.set(1, 1)
    test_cache_2.set(2, 2)

    test_cache_2.get(1)
    test_cache_2.get(2)

    test_cache_2.set(3, 3)

    assert test_cache_2.get(3) == 3

    # Test 3 - Given LRU, when trying to set with None for key, throw exception
    test_cache_3 = LRU_Cache(4)

    try:
        test_cache_3.set(None, 123)
        assert False
    except TypeError as ex:
        assert str(ex) == '"key" parameter must not be None'


    # Test 3 - Given LRU, when trying to set with None for key, throw exception
    test_cache_3 = LRU_Cache(4)

    try:
        test_cache_3.set(None, 123)
        assert False
    except TypeError as ex:
        assert str(ex) == '"key" parameter must not be None'

    # Test 4 - When attempt to start LRU with None, throw TypeError exception
    
    try:
        LRU_Cache(None)
        assert False
    except TypeError as ex:
        assert str(ex) == 'capacity must not be None'

    # Test 5 - When attempt to start LRU with 0, throw ValueError exception
    
    try:
        LRU_Cache(0)
        assert False
    except ValueError as ex:
        assert str(ex) == 'capacity must be a positive integer'

    # Test 6 - When attempt to start LRU with negative number, throw ValueError exception
    try:
        LRU_Cache(-1)
        assert False
    except ValueError as ex:
        assert str(ex) == 'capacity must be a positive integer'

if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
