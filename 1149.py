# BOJ 1149 RGB거리

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(3)]
for i in range(3):
    dp[i][0] = rgb[0][i]
for n in range(1, N):
    dp[0][n] = min(dp[1][n - 1], dp[2][n - 1]) + rgb[n][0]
    dp[1][n] = min(dp[0][n - 1], dp[2][n - 1]) + rgb[n][1]
    dp[2][n] = min(dp[0][n - 1], dp[1][n - 1]) + rgb[n][2]
print(min(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))