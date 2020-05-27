# BOJ 9252 LCS 2

S1 = input()
L1 = len(S1)
S2 = input()
L2 = len(S2)
table = [[0] * (L1 + 1) for _ in range(L2 + 1)]
for i in range(L2):
    for j in range(L1):
        if S1[j] == S2[i]:
            table[i + 1][j + 1] = table[i][j] + 1
        else:
            table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
result = table[L2][L1]
print(result)
answer = ''
y = L2
x = L1
while result > 0:
    if table[y][x - 1] == result - 1 and table[y - 1][x] == result - 1:
        answer = S1[x - 1] + answer
        result, y, x = result - 1, y - 1, x - 1
    else:
        if table[y - 1][x] > table[y][x - 1]:
            y -= 1
        else:
            x -= 1
print(answer)