# BOJ 1922 네트워크 연결

from heapq import heappush, heappop
INF = 1e9

def prim():
    result = 0
    dist = [0] + [INF] * N
    q = []
    heappush(q, [0, 1])
    while q:
        cost, pos = heappop(q)
        if dist[pos] == INF:
            dist[pos] = cost
            result += cost
            for p, c in route[pos]:
                if dist[p] == INF:
                    heappush(q, [c, p])
    return result

N = int(input())
M = int(input())
route = [[] for _ in range(N + 1)]
for m in range(M):
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    route[b].append([a, c])
print(prim())