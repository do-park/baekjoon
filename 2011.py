# BOJ 2011 암호코드

N = list(map(int, input()))
L = len(N)
dp = [[0, 0] for _ in range(L + 1)]
dp[0][0] = 1
for n in range(L):
    if N[n] != 0:
        dp[n + 1][0] = sum(dp[n])
    if n > 0 and N[n - 1] != 0 and (N[n - 1] * 10 + N[n]) < 27:
        dp[n + 1][1] = sum(dp[n - 1])
print(sum(dp[L]) % 1000000)