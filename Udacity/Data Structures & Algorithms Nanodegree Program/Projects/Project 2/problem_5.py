from datetime import timezone, datetime
import hashlib
from typing import List


def get_utc() -> datetime:
    return datetime.now(timezone.utc)


class Block:

    def __init__(self, data: str, previous_hash: str, timestamp: datetime = get_utc()):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self) -> str:
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return f'<Block timestamp={self.timestamp}  ' +\
               f'previous_hash[:10]="{self.previous_hash[:10]}"' +\
               f' hash[:10]="{self.hash[:10]}">'


class Blockchain:
    def __init__(self):
        self.head = None  # First block
        self.tail = None  # Latest block
        self.size = 0

    def add(self, data: str):
        if data is None:
            raise TypeError('data must not be None')

        if type(data) is int:
            raise TypeError(
                'data must not be of type "int". "data" parameter must be of type "str"')

        prev_hash = self.tail.hash if self.tail else '0'

        block = Block(data, prev_hash)

        if self.head is None:
            self.head = block
            self.tail = block
        else:
            self.tail.next = block
            self.tail = block

        self.size += 1

    def __str__(self):
        block = self.head
        r = f'<Blockchain size={self.size}>'
        t = ['\n']
        while block:
            t.append('\t' + str(block))
            block = block.next

        return r + '\n'.join(t)


def test():
    # Test 1 - Assert blockchain is created with correct properties
    blockchain_1 = Blockchain()

    assert blockchain_1.size == 0
    assert blockchain_1.head == None
    assert blockchain_1.tail == None

    # Test 2 - Given two values, assert two blocks are created and that "previous_hash" of the second block is equal to the "hash" of the first block
    blockchain_2 = Blockchain()

    test_data = [
        'Hello',
        'Its me'
    ]

    for data in test_data:
        blockchain_2.add(data)

    assert blockchain_2.size == 2
    assert blockchain_2.head.previous_hash == '0'
    assert blockchain_2.head.next == blockchain_2.tail
    assert blockchain_2.head.hash == blockchain_2.tail.previous_hash

    # Test 3 - Given int parameter, raise TypeError exception
    blockchain_3 = Blockchain()
    try:
        blockchain_3.add(12341234)
    except TypeError as ex:
        assert str(
            ex) == 'data must not be of type "int". "data" parameter must be of type "str"'

    # Test 4 - Given None parameter, raise TypeError exception
    blockchain_4 = Blockchain()

    try:
        blockchain_4.add(None)
        assert False
    except TypeError as ex:
        assert str(ex) == 'data must not be None'


if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
