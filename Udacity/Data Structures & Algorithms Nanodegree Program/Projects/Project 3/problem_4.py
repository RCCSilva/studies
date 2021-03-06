def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index_0 = 0
    index_2 = len(input_list) - 1

    i = 0

    while i <= index_2:
      if input_list[i] == 0:
        swap(input_list, index_0, i)
        i += 1 
        index_0 += 1
      elif input_list[i] == 2:
        swap(input_list, index_2, i)
        index_2 -= 1
      else:
        i += 1

    return input_list

def swap(arr: list, a: int, b: int) -> None:
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([1])
test_function([2])
test_function([])