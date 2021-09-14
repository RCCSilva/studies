import sys
from typing import List


def huffman_encoding(data):
    if data == '':
        return '', None

    count_table = {}

    for char in data:
        if char in count_table:
            count_table[char] += 1
        else:
            count_table[char] = 1

    nodes = [Node(count_table[x], x) for x in count_table]

    tree = create_huffman_tree(nodes)

    char_to_huffman = {}

    if tree.left or tree.right:
        get_huffman_values(tree, '', char_to_huffman)
    else:
        char_to_huffman[char] = '0'

    bin_rep = ''
    for char in data:
        bin_rep += char_to_huffman[char]

    return bin_rep, tree


def huffman_decoding(data, tree):
    if data == '':
        return ''

    decoded = ''

    if not (tree.left or tree.right):
        for _ in data:
            decoded += tree.char
        return decoded

    node = tree

    for char in data:
        if char == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded += node.char
            node = tree

    return decoded


class Node:
    def __init__(self, count, char=None):
        self.char = char
        self.count = count
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node char={self.char} count={self.count}>'

    def __lt__(self, other):
        if self.count != other.count or not (self.char and other.char):
            return self.count < other.count
        else:
            return self.char < other.char


def create_huffman_tree(node_list):
    if len(node_list) == 1:
        return node_list[0]

    sf = sorted(node_list, reverse=True)

    smaller_1 = sf.pop()
    smaller_2 = sf.pop()

    new_node = Node(smaller_1.count + smaller_2.count)
    new_node.left = smaller_1
    new_node.right = smaller_2

    sf.append(new_node)

    return create_huffman_tree(sf)


def get_huffman_values(root: Node, _bin, _map):
    if root is None:
        return

    if root.char is not None:
        _map[root.char] = _bin

    get_huffman_values(root.left, _bin + '0', _map)
    get_huffman_values(root.right, _bin + '1', _map)


def test():
    # Test 1 - Given equal char sentence, return correct encoded data and return correct decoded data
    test_sentence = 'AAAA'
    encoded_data, tree = huffman_encoding(test_sentence)
    assert encoded_data != ''

    decoded_data = huffman_decoding(encoded_data, tree)

    assert test_sentence == decoded_data, decoded_data

    # Test 2 - Given even size, return correct encoded data and return correct decoded data
    test_sentence = 'ABBA'
    encoded_data, tree = huffman_encoding(test_sentence)
    assert encoded_data != ''

    decoded_data = huffman_decoding(encoded_data, tree)

    assert test_sentence == decoded_data, decoded_data

    # Test 3 - Given equal char sentence, return correct encoded data and return correct decoded data
    test_sentence = 'ABCBA'
    encoded_data, tree = huffman_encoding(test_sentence)
    assert encoded_data != ''

    decoded_data = huffman_decoding(encoded_data, tree)

    assert test_sentence == decoded_data, decoded_data

    # Test 4 - Given valid test sentence, return correct encoded data and return correct decoded data
    test_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    encoded_data, tree = huffman_encoding(test_sentence)

    assert encoded_data == '1010101010101000100100111111111111111000000010101010101'

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == test_sentence

    # Test 5 - Given sentence composed of special characters, encode e decore it correctly
    test_sentence = 'çáàãâêîô'
    encoded_data, tree = huffman_encoding(test_sentence)

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == test_sentence


    # Test 6 - Given an empty string as the input sentence, encode e decore it correctly
    test_sentence = ''
    encoded_data, tree = huffman_encoding(test_sentence)

    assert encoded_data == ''
    assert tree is None

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == test_sentence

if __name__ == "__main__":
    print(f'Starting "{__file__}" tests... ', end='')
    test()
    print('Finished!')
