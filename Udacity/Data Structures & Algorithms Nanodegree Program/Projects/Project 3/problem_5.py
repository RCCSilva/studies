import string

class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.char = None
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            trie_node = TrieNode()
            trie_node.char = char
            self.children[char] = trie_node

    def suffixes(self):
        # Recursive function that collects the suffix for
        # all complete words below this point
        result_list = []
        self.__find_suffixes(self, '', result_list)

        return result_list

    def __find_suffixes(self, node, prev_chars: str, result_list: list) -> None:
        if len(node.children) == 0 or node.is_word:
            if prev_chars != '':
                result_list.append(prev_chars)

        for child in node.children.values():
            self.__find_suffixes(child, prev_chars + child.char, result_list)

# The Trie itself containing the root node and insert/find functions


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word) -> None:
        # Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix) -> TrieNode:
        # Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if node is None:
                break
            node = node.children.get(char)

        return node

# Test 1
my_trie_1 = Trie()
word_list_1 = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list_1:
    my_trie_1.insert(word)

assert set(my_trie_1.find('').suffixes()) == set(word_list_1)
assert set(my_trie_1.find('a').suffixes()) == {"nt", "nthology", "ntagonist", "ntonym"}
assert set(my_trie_1.find('ant').suffixes()) == {"hology", "agonist", "onym"}
assert set(my_trie_1.find('f').suffixes()) == {"un", "unction", "actory"}
assert set(my_trie_1.find('t').suffixes()) == {"rie", "rigger", "rigonometry", "ripod"}

# Test 2
my_trie_2 = Trie()
word_list_2 = []
for word in word_list_2:
    my_trie_2.insert(word)

assert len(my_trie_2.find('').suffixes()) == 0
for char in string.ascii_letters:
    assert my_trie_2.find(char) is None

# Test 3
my_trie_3 = Trie()
word_list_3 = ['one']
for word in word_list_3:
    my_trie_3.insert(word)

assert len(my_trie_3.find('').suffixes()) == 1
for char in string.ascii_letters.replace('o', ''):
    assert my_trie_3.find(char) is None
assert my_trie_3.find('o').suffixes() == ['ne']
