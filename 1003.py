# BOJ 1003 피보나치 함수

T = int(input())
N = [int(input()) for _ in range(T)]
mx = max(max(N), 1)
dp = [[0] * (mx + 1) for _ in range(2)]
dp[0][0], dp[1][1] = 1, 1
for i in range(2, mx + 1):
    dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
    dp[1][i] = dp[1][i - 1] + dp[1][i - 2]
for n in N:
    print(dp[0][n], dp[1][n])