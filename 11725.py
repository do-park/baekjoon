# BOJ 11725 트리의 부모 찾기

def dfs(start, route):
    parent = [[] for _ in range(N + 1)]
    stack = [start]
    while stack:
        V = stack.pop()
        for r in route[V]:
            parent[r].append(V)
            stack.append(r)
            route[r].remove(V)
    return parent


N = int(input())
route = [[] for _ in range(N + 1)]
for n in range(N - 1):
    x, y = map(int, input().split())
    route[x].append(y)
    route[y].append(x)
parent = dfs(1, route)[2:]
for i in range(N - 1):
    print(* parent[i])