# BOJ 2759 계단 오르기

N = int(input())
stairs = [0]
for n in range(N):
    stairs.append(int(input()))
dp = [[0] * (N + 1) for _ in range(2)]
dp[0][1] = stairs[1]
for n in range(2, N + 1):
    dp[0][n] = max(dp[0][n - 2], dp[1][n - 2]) + stairs[n]
    dp[1][n] = dp[0][n - 1] + stairs[n]
print(max(dp[0][N], dp[1][N]))