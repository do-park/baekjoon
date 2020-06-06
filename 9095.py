# BOJ 9095 1, 2, 3 더하기

T = int(input())
N = [int(input()) for _ in range(T)]
mx = max(N)
dp = [0, 1, 2, 4] + [0] * (mx - 3)
for i in range(4, mx + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for n in N:
    print(dp[n])