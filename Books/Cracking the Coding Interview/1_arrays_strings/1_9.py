def is_substring(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False # Or None. Or throw exception

    if len(s1) > len(s2):
        return False

    diff = len(s1)

    for final in range(diff, len(s2) + 1):

        attempt = s2[final - diff:final]

        for i, char in enumerate(attempt):
            if s1[i] != char:
                break

            if (i == len(s1) - 1):
                return True

    return False


if __name__ == '__main__':
    print(is_substring('ab', 'abcd'))
    print(is_substring('bc', 'abcd'))
    print(is_substring('cd', 'abcd'))
    print(is_substring('dc', 'abcd'))
    print(is_substring('ba', 'abcd'))
    print(is_substring('abcde', 'abcd'))
    print(is_substring(None, 'abcd'))
    print(is_substring('abcde', None))