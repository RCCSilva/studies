from typing import List

def rotate(m: List[List[int]]) -> None:
    i = 0
    j = 0
    ii = len(m) - 1
    jj = 0

    response = []

    while i < len(m):
        response.append([])
        while j < len(m):
            response[i].append(m[ii][jj])
            print(response)

            j += 1
            ii -= 1

        i += 1
        j = 0
        ii = len(m) - 1
        jj += 1

    return response

if __name__ == '__main__':
    m = [
        [1,2,3],
        [1,2,3],
        [1,2,3],
    ]

    print(rotate(m))
