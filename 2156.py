# BOJ 2156 포도주 시식

N = int(input())
wine = [0]
for n in range(N):
    wine.append(int(input()))
wine += [0]
dp = [[0] * (N + 2) for _ in range(3)]
dp[1][1] = wine[1]
for n in range(2, N + 2):
    dp[0][n] = max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])
    dp[1][n] = max(dp[0][n - 2], dp[1][n - 2], dp[2][n - 2]) + wine[n]
    dp[2][n] = dp[1][n - 1] + wine[n]
print(max(dp[0][N + 1], dp[1][N + 1], dp[2][N + 1]))