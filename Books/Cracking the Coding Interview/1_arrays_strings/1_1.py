# Time: O(n), Memory: O(n)
# I think (not sure about this), that it's memory O(n) for strings less than 256 chars, given that
# we are talking about ASCII strings. For strings, greater than that, we are guaranteed that will be
# no more than 256, which would turn it into a O(1) for memory. I think hahahaah

def is_unique_set(string: str) -> bool:
    char_set = set()
    for char in string:
        if char in char_set:
            return False

        char_set.add(char)

    return True

# Time: O(n log(n)), Memory: O(1)

def is_unique_sort(string: str) -> bool:
    string_list = list(string)
    string_list.sort()

    for i in range(len(string_list) - 1):
        if string_list[i] == string_list[i + 1]:
            return False

    return True

if __name__ == '__main__':
    not_unique = 'the not unique string'
    unique = 'asdfghjklç poiuytrewq'

    print(is_unique_sort(not_unique))
    print(is_unique_set(not_unique))

    print(is_unique_sort(unique))
    print(is_unique_set(unique))
