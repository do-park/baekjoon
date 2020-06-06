# BOJ 2302 극장 좌석

N = int(input())
M = int(input())
fixed = [0] + [int(input()) for _ in range(M)] + [N + 1]
dp = [1, 1, 2] + [0] * (N - 2)
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
result = 1
for i in range(M + 1):
    result *= (dp[fixed[i + 1] - fixed[i] - 1])
print(result)