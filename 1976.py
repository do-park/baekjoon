# BOJ 1976 여행 가자

def find(x):
    if parent[x] < 0:
        return x
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

N = int(input())
parent = [-1] * N
M = int(input())
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            union(i, j)
cities = list(map(int, input().split()))
for m in range(M - 1):
    if find(cities[m] - 1) != find(cities[m + 1] - 1):
        print('NO')
        break
else:
    print('YES')