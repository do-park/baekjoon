# BOJ 11053 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))