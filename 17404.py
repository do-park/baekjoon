# BOJ 17404 RGB거리 2

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
result = 1e9
for j in range(3):
    for k in range(3):
        dp[0][k] = rgb[0][k] if j == k else 1001
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]
    dp[N - 1][j] = 1001000
    result = min(min(dp[N - 1]), result)
print(result)