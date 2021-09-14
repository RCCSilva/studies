def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    search_left = input_list[-1] < number
    max_left_index = search_max_left_index(input_list)
    result = None

    if search_left:
        result = search(input_list, number, 0, max_left_index)
    else:
        result = search(input_list, number, max_left_index, len(input_list))

    return result


def search_max_left_index(arr: list) -> int:
    if arr[0] < arr[-1]:
        return len(arr) - 1

    i = len(arr) // 2

    if is_pivot(arr, i):
        return i

    if arr[i] < arr[-1]:
        return search_max_left_index(arr[:i])
    elif arr[i] > arr[-1]:
        return search_max_left_index(arr[i + 1:])


def is_pivot(arr: list, index: int) -> bool:
    return arr[index] > arr[index + 1]


def search(arr, target, start, end):
    if start > end:
        return -1

    i = (start + end) // 2
    if arr[i] == target:
        return i
    elif target > arr[i]:
        return search(arr, target, i + 1, end)
    else:
        return search(arr, target, start, i)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    assert linear_search(input_list, number) == rotated_array_search(
        input_list, number)
    print("Pass")



test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, -1, 2, 3, 4], -1])
test_function([[-3, -2, -1, -4, -5, -6], 10])
test_function([[-3, -2, -1, -4, -5, -6], -1])
test_function([[-3, -2, -1, -6, -5, -4], -4])
test_function([[10], 10])
test_function([[-10], -10])
test_function([[], 10])
