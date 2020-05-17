# BOJ 1504 특정한 최단 경로

from heapq import heappush, heappop
INF = 1e9

def dijkstra(a, b):
    dist = [INF] * V
    dist[a - 1] = 0
    q = []
    heappush(q, [0, a - 1])
    while q:
        cost, pos = heappop(q)
        for p, c in route[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
    return dist[b - 1]

V, E = map(int, input().split())
route = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    route[u - 1].append([v - 1, w])
    route[v - 1].append([u - 1, w])
V1, V2 = map(int, input().split())
result1 = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, V)
result2 = dijkstra(1, V2) + dijkstra(V2, V1) + dijkstra(V1, V)
result = min(result1, result2, INF)
print(result if result != INF else -1)