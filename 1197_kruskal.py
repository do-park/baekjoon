INF = 1e9

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
    for e in range(E):
        w, x, y = edge[e]
        if find_set(x) == find_set(y) and find_set(x) > 0:
            continue
        result += w
        MST.append(edge[e])
        union(x, y)
        count += 1
        if count == V - 1:
            break
    return result


V, E = map(int, input().split())
edge = []
for e in range(E):
    a, b, w = map(int, input().split())
    edge.append([w, a, b])
edge.sort(key=lambda x: x[0])
parent = [0] + [-1] * V
print(kruskal())