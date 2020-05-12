# BOJ 1238 파티

from heapq import heappush, heappop
INF = 1e9

def dijkstra(x):
    dist = [INF] * N
    dist[x] = 0
    q = []
    heappush(q, [0, x])
    while q:
        cost, pos = heappop(q)
        for p, c in road[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
    return dist

N, M, X = map(int, input().split())
road = [[] for n in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    road[u - 1].append([v - 1, t])
result = [0] * N
for n in range(N):
    ret = dijkstra(n)
    if n == X - 1:
        for i, r in enumerate(ret):
            result[i] += r
    else:
        result[n] += ret[X - 1]
print(max(result))