# BOJ 4386 별자리 만들기_prim

from heapq import heappush, heappop
INF = 1e9

def prim():
    dist = [INF] * N
    q = []
    heappush(q, [0, 0])
    while q:
        cost, pos = heappop(q)
        if dist[pos] == INF:
            dist[pos] = cost
            for i in range(N):
                if dist[i] == INF:
                    heappush(q, [adj[pos][i], i])
    return sum(dist)


N = int(input())
stars = []
for n in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))
adj = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        adj[i][j] = adj[j][i] = round(((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2), 2)
print(prim())