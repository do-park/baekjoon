# SWEA 1912 연속합

N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = numbers[0]
for n in range(1, N):
    dp[n] = max(0, dp[n - 1]) + numbers[n]
print(max(dp))