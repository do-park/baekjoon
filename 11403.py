# BOJ 11403 경로 찾기

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][n] and adj[n][j]:
                adj[i][j] = 1
for i in range(N):
    print(*adj[i])