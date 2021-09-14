
# Time: O(n log(n)). Memory: O(1). Maybe O(n) since the strings are copied?
# To achive O(1) memory, it would need to be possible to sort the string directly.
# I'm afraid that's not possible with Python. C++ maybe?
def is_permutation_sort(a: str, b: str):
    if a is None or b is None:
        return False

    if len(a) != len(b):
        return False

    a_list = list(a)
    b_list = list(b)

    a_list.sort()
    b_list.sort()

    for x, y in zip(a_list, b_list):
        if x != y:
            return False

    return True


# Time: O(n). Memory: O(n)
def is_permutation_map(a: str, b: str):
    if a is None or b is None:
        return False

    if len(a) != len(b):
        return False

    def build_char_map(string: str):
    char_map = {}
        for char in string:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        return char_map


    char_map = build_char_map(a)

    for char in b:
        if char not in char_map:
            return False
        if char_map[char] == 0:
            return False

        char_map[char] -= 1

    return True


if __name__ == '__main__':
    #

    a = 'asdfgh'
    b = 'hgfdsa'

    print(is_permutation_map(a, b))
    print(is_permutation_sort(a, b))

    a = 'asdfgha'
    b = 'hgfdsa'

    print(is_permutation_map(a, b))
    print(is_permutation_sort(a, b))

    a = None
    b = 'hgfdsa'

    print(is_permutation_map(a, b))
    print(is_permutation_sort(a, b))

    a = 'asdfg'
    b = None

    print(is_permutation_map(a, b))
    print(is_permutation_sort(a, b))

    a = 'hjklçgfdsa'
    b = 'asdfghjklç'

    print(is_permutation_map(a, b))
    print(is_permutation_sort(a, b))