# BOJ 4386 별자리 만들기_kruskal


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
    for a in range(len(adj)):
        w, x, y = adj[a]
        if find_set(x) == find_set(y):
            continue
        result += w
        MST.append(adj[a])
        union(x, y)
        count += 1
        if count == N - 1:
            break
    return result


N = int(input())
stars = []
for n in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))
adj = []
for i in range(N):
    for j in range(i + 1, N):
        adj.append((round(((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2), 2), i, j))
adj.sort(key=lambda x: x[0])
parent = [-1] * N
print(kruskal())