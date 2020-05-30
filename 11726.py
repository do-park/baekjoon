# BOJ 11726 2*n 타일링

N = int(input())
dp = [0, 1, 2] + [0] * N
for n in range(3, N + 3):
    dp[n] = (dp[n - 1] + dp[n - 2]) % 10007
print(dp[N])