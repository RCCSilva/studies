import sys

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    if number < 0:
        return None

    def _sqrt(lower_bound, upper_bound):
        p = (upper_bound + lower_bound) // 2

        t0 = p ** 2
        t1 = (p + 1) ** 2

        if t0 <= number < t1:
            return p

        if number > t0:
            return _sqrt(p, upper_bound)
        else:
            return _sqrt(lower_bound, p)

    return _sqrt(0, number + 1)


assert None == sqrt(-1)
assert None == sqrt(-2147483647) # Min 32 bit int
assert 46340 == sqrt(2147483647) # Max 32 bit integer
assert 0 == sqrt(0)
assert 1 == sqrt(1)
assert 1 == sqrt(2)
assert 1 == sqrt(3)
assert 2 == sqrt(4)
assert 2 == sqrt(5)
assert 3 == sqrt(9)
assert 4 == sqrt(16)
assert 5 == sqrt(27)
