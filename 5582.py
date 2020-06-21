# BOJ 5582 공통 부분 문자열

S1 = list(map(str, input()))
L1 = len(S1)
S2 = list(map(str, input()))
L2 = len(S2)
dp = [[0] * (L1 + 1) for _ in range(L2 + 1)]
result = 0
for i in range(L2):
    for j in range(L1):
        if S1[j] == S2[i]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            result = max(result, dp[i + 1][j + 1])
print(result)