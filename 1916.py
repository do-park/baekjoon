# BOJ 1916 최소 비용 구하기

from heapq import heappush, heappop
INF = 1e9

def dijkstra(s, e):
    dist = [INF] * V
    dist[s - 1] = 0
    q = []
    heappush(q, [0, s - 1])
    while q:
        cost, pos = heappop(q)
        for p, c in route[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
    return dist[e - 1]

V = int(input())
E = int(input())
route = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    route[u - 1].append([v - 1, w])
S, E = map(int, input().split())
print(dijkstra(S, E))