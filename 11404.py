# BOJ 11404 플로이드
INF = 1e9

N = int(input())
M = int(input())
adj = [[INF] * (N + 1) for _ in range(N + 1)]
for m in range(M):
    a, b, c = map(int, input().split())
    if adj[a][b] > c:
        adj[a][b] = c
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            adj[i][j] = min(adj[i][j], adj[i][n] + adj[n][j])
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j or adj[i][j] == INF:
            print(0, end=' ')
        else:
            print(adj[i][j], end=' ')
    print()