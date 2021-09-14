from typing import List

def zero_matrix(m: List[List[int]]):
    if not m:
        return None

    i_set = set()
    j_set = set()

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                i_set.add(i)
                j_set.add(j)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if i in i_set or j in j_set:
                m[i][j] = 0


if __name__ == '__main__':
    m = [
        [0,2,3],
        [3,2,2],
        [2,3,0]
    ]

    zero_matrix(m)

    print(m)