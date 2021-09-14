def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return []

    arr = sort(input_list)

    x = []
    y = []

    for i, n in enumerate(arr):
        if i % 2 == 0:
            x.append(n)
        else:
            y.append(n)

    return [convert_list_to_int(x), convert_list_to_int(y)]


def sort(arr: list) -> list:
    return merge_sort(arr)


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    p = len(arr) // 2
    return __merge_sorted_arrays(merge_sort(arr[:p]), merge_sort(arr[p:]))


def __merge_sorted_arrays(a: list, b: list) -> list:
    ia = 0
    ib = 0

    result = []

    for _ in range(len(a) + len(b)):
        if ib > len(b) - 1 or (ia < len(a) and a[ia] > b[ib]):
            result.append(a[ia])
            ia += 1
        else:
            result.append(b[ib])
            ib += 1

    return result


def convert_list_to_int(arr: list) -> int:
    result = 0
    for i, x in enumerate(arr[::-1]):
        result += x * (10 ** i)

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert sum(output) == sum(solution)
    print("Pass")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 9], [9, 9]])
test_function([[1], []])
test_function([[], []])
