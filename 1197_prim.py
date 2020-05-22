# BOJ 1197 최소 스패닝 트리

from heapq import heappush, heappop
INF = 1e9

def prim():
    dist = [INF] * (V + 1)
    q = []
    heappush(q, [0, 1])
    result = 0
    while q:
        cost, pos = heappop(q)
        if dist[pos] == INF:
            dist[pos] = cost
            result += cost
            for p, c in route[pos]:
                if dist[p] > cost:
                    heappush(q, [c, p])
    return result


V, E = map(int, input().split())
route = [[] for _ in range(V + 1)]
for e in range(E):
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    route[b].append([a, c])
print(prim())
