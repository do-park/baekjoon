# BOJ 11779 최소비용 구하기 2

from heapq import heappush, heappop
INF = 1e9

def dijkstra(S, E):
    dist = [INF] * V
    before = [-1] * V
    dist[S - 1] = 0
    q = []
    heappush(q, [0, S - 1])
    while q:
        cost, pos = heappop(q)
        for p, c in route[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
                before[p] = pos
    print(dist[E - 1])
    result = []
    i = E - 1
    while True:
        if before[i] == -1:
            result.append(i + 1)
            return result
        result.append(i + 1)
        i = before[i]

V = int(input())
E = int(input())
route = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    route[u - 1].append([v - 1, w])
S, E = map(int, input().split())
result = dijkstra(S, E)
print(len(result))
print(* result[::-1])