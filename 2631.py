# BOJ 2631 줄세우기

N = int(input())
children = [int(input()) for _ in range(N)]
dp = [0] * N
for i in range(1, N):
    for j in range(i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp) - 1)