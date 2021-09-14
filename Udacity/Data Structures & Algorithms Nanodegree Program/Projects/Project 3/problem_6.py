def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None

    for x in ints:
      if min is None or min > x:
        min = x
      if max is None or max < x:
        max = x

    return min, max

## Example Test Case of Ten Integers
import random

for _ in range(5):
    l = [i for i in range(0, 10)]
    random.shuffle(l)
    assert (0, 9) == get_min_max(l)


assert (None, None) == get_min_max([])
assert (0, 0) == get_min_max([0])
assert (-1, -1) == get_min_max([-1])
assert (1, 1) == get_min_max([1])
assert (0, 1) == get_min_max([1,0])
assert (0, 0) == get_min_max([0,0])
assert (-1, 1) == get_min_max([-1,1])
assert (-2147483648, 2147483647) == get_min_max([-2147483648, 2147483647]) # Min and max 32 bit integers