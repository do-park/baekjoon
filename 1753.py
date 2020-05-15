# BOJ 1753 최단경로

from heapq import heappush, heappop
INF = 1e9

def dijkstra(k):
    dist = [INF] * V
    dist[k - 1] = 0
    q = []
    heappush(q, [0, k - 1])
    while q:
        cost, pos = heappop(q)
        for p, c in route[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
    return dist

V, E = map(int, input().split())
K = int(input())
route = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    route[u - 1].append([v - 1, w])
for d in dijkstra(K):
    print(d if d != INF else 'INF')