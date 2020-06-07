# BOJ 1915 가장 큰 정사각형

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
result = maps[0][0]
for n in range(1, N):
    for m in range(1, M):
        if maps[n][m]:
            maps[n][m] = min(maps[n - 1][m], maps[n][m - 1], maps[n - 1][m - 1]) + 1
            result = max(result, maps[n][m])
print(result ** 2)