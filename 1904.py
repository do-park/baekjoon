# BOJ 1904 01타일

N = int(input())
dp = [0, 1, 2] + [0] * (N - 2)
for n in range(3, N + 1):
    dp[n] = (dp[n - 1] + dp[n - 2]) % 15746
print(dp[N])