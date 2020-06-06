# BOJ 9461 파도반 수열

T = int(input())
N = [int(input()) for _ in range(T)]
mx = max(N)
dp = [0, 1, 1] + [0] * (mx - 2)
for i in range(3, mx + 1):
    dp[i] = dp[i - 2] + dp[i - 3]
for n in N:
    print(dp[n])