# BOJ 17140 이차원 배열과 연산

from collections import Counter

def R(A):
    new_A = []
    maxi = 0
    for a in A:
        new_row = []
        counter = sorted(list(Counter(a).items()), key=lambda x: (x[1], x[0]))
        for num, cnt in counter:
            if num == 0:
                continue
            new_row.append(num)
            new_row.append(cnt)
        maxi = max(maxi, len(new_row))
        new_A.append(new_row)
    for a in new_A:
        if len(a) < maxi:
            a += [0] * (maxi - len(a))
    return new_A

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = [list(map(int, input().split())) for _ in range(3)]
for t in range(101):
    row = len(A)
    col = len(A[0])
    if r < row and c < col:
        if A[r][c] == k:
            print(t)
            break
    if row >= col:
        A = R(A)
    else:
        A = list(map(list, zip(*A)))
        A = R(A)
        A = list(map(list, zip(*A)))
else:
    print(-1)