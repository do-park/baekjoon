# BOJ 1965 상자넣기

N = int(input())
boxes = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))