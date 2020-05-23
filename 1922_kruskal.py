# BOJ 1922 네트워크 연결

def find_set(x):
    if parent[x] < 0:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return

def kruskal():
    MST = []
    result = 0
    count = 0
    for m in range(M):
        a, b, c = route[m]
        if find_set(a) == find_set(b):
            continue
        result += c
        MST.append(route[m])
        union(a, b)
        count += 1
        if count == N - 1:
            break
    return result


N = int(input())
M = int(input())
route = []
for m in range(M):
    a, b, c = map(int, input().split())
    route.append([a, b, c])
route.sort(key=lambda x: x[2])
parent = [0] + [-1] * N
print(kruskal())