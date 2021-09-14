from typing import List

def urlfy(string_list: List[str]) -> str:
    if not string_list:
        return None

    def start_fast(string: str) -> int:
        for i in range(len(string))[::-1]:
            if string[i] != ' ':
                return i

    slow = len(string_list) - 1
    fast = start_fast(string_list)


    space_chars = ['0', '2', '%']

    while slow > fast >= 0:
        if string_list[fast] == ' ':
            for char in space_chars:
                string_list[slow] = char
                slow -= 1
        else:
            temp = string_list[slow]
            string_list[slow] = string_list[fast]
            string_list[fast] = temp
            slow -= 1

        fast -= 1


    return ''.join(string_list)

if __name__ == '__main__':
    print(urlfy(list('my first test    ')))
    print(urlfy(list(' myfirsttest  ')))
    print(urlfy(list('m y f i r s t t e s t                    ')))
