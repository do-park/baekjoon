# BOJ 11052 카드 구매하기

N = int(input())
P = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    for j in range(1, i // 2 + 1):
        P[i] = max(P[i], P[i - j] + P[j])
print(P[-1])