# BOJ 6497 전력난_prim
# 시간 초과

from heapq import heappush, heappop
INF = 1e9

def prim():
    result = 0
    dist = [INF] * M
    q = []
    heappush(q, [0, 0])
    while q:
        cost, pos = heappop(q)
        if dist[pos] == INF:
            dist[pos] = cost
            result += cost
            for route in routes[pos]:
                c, p = route
                if dist[p] == INF:
                    heappush(q, [c, p])
    return result


while True:
    M, N = map(int, input().split())
    if M == 0:
        break
    routes = [[] for _ in range(M)]
    before = 0
    for n in range(N):
        x, y, z = map(int, input().split())
        routes[x].append([z, y])
        routes[y].append([z, x])
        before += z
    print(before - prim())