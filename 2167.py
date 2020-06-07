# BOJ 2167 2차원 배열의 합

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = dp[n - 1][m] + dp[n][m - 1] + maps[n - 1][m - 1] - dp[n - 1][m - 1]
K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])