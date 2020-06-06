# BOJ 11057 오르막 수

N = int(input())
dp = [1] * 10
for n in range(1, N):
    tp = [0] * 10
    tp[0] = sum(dp)
    for i in range(1, 10):
        tp[i] = (tp[i - 1] - dp[i - 1]) % 10007
    dp = tp
print((sum(dp)) % 10007)