import string



def add_or_increment(char: str, m: dict) -> dict:
    if char not in m:
        m[char] = 1
    else:
        m[char] += 1

    return m


def compress(st: str) -> str:
    char_amount = {}

    for char in st:
        char_amount = add_or_increment(char, char_amount)

    summ = 0

    for amount in char_amount.values():
        summ += (2 - amount)

    if summ >= 0:
        return st

    response = []

    for char in string.ascii_lowercase:
        if char in char_amount:
            response.append(char + str(char_amount[char]))

    return ''.join(response)
    

if __name__ == '__main__':
    print(compress('aaaaaabbcccccccccccccccccc'))
    print(compress('ab'))
    print(compress('qwertyuiopasdfghjklc'))
    print(compress('abcdddddd'))