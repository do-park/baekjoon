# BOJ 1717 집합의 표현

def find(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return


N, M = map(int, input().split())
parent = [-1] * (N + 1)
for m in range(M):
    f, a, b = map(int, input().split())
    if f:
        a = find(a)
        b = find(b)
        print('YES' if a == b else 'NO')
    else:
        union(a, b)
