# BOJ 1699 제곱수의 합

N = int(input())
dp = [1e9] * (N + 1)
dp[0] = 0
sqr = []
i = 1
while i * i <= N:
    sqr.append(i * i)
    i += 1
for s in sqr:
    for i in range(s, N + 1):
        dp[i] = min(dp[i - s] + 1, dp[i])
print(dp[-1])