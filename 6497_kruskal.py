# BOJ 6497 전력난_kruskal

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return
    if x < y:
        parent[x] += parent[y]
        parent[y] = x
        return
    else:
        parent[y] += parent[x]
        parent[x] = y
        return


def kruskal():
    result = 0
    count = 0
    for route in routes:
        w, x, y = route
        if find_parent(x) == find_parent(y):
            continue
        result += w
        count += 1
        union(x, y)
        if count == M - 1:
            break
    return result


while True:
    M, N = map(int, input().split())
    if M == 0:
        break
    routes = []
    before = 0
    for n in range(N):
        x, y, z = map(int, input().split())
        routes.append([z, x, y])
        before += z
    routes.sort(key=lambda x: x[0])
    parent = [-1] * N
    print(before - kruskal())