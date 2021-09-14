def is_one(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False

    i = 0
    j = 0

    count = 0

    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if len(a) > len(b):
                i += 1
            elif len(b) > len(a):
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        else:
            i += 1
            j += 1

  return abs(i - j) + count <= 1

if __name__ == '__main__':
    print(is_one('abx', 'abzz'))