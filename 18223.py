# BOJ 18223 민준이와 마산 그리고 건우

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


V, E, P = map(int, input().split())
route = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    route[u - 1].append([v - 1, w])
    route[v - 1].append([u - 1, w])
result1 = dijkstra(1, V)
result2 = dijkstra(1, P) + dijkstra(P, V)
print('SAVE HIM' if result2 <= result1 else 'GOOD BYE')