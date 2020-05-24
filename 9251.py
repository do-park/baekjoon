# BOJ 9251 LCS

S1 = input()
L1 = len(S1)
S2 = input()
L2 = len(S2)
table = [[0] * (L1 + 1) for _ in range(L2 + 1)]
for i in range(L2):
    for j in range(L1):
        if S2[i] == S1[j]:
            table[i + 1][j + 1] = table[i][j] + 1
        else:
            table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
print(table[L2][L1])