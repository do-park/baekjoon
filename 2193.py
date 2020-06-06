# BOJ 2193 이친수

N = int(input())
dp = [0, 1] + [0] * (N - 1)
for n in range(2, N + 1):
    dp[n] = dp[n - 1] + dp[n - 2]
print(dp[-1])