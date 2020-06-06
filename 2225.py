# BOJ 2225 합분해

N, K = map(int, input().split())
dp = [1] * (N + 1)
for k in range(1, K):
    for n in range(1, N + 1):
        dp[n] = (dp[n - 1] + dp[n]) % 1000000000
print(dp[-1])