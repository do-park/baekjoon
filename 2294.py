# BOJ 2294 동전 2

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [100001] * (K + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])
print(dp[K] if dp[K] < 100001 else -1)