# BOJ 10844 쉬운 계단 수

N = int(input())
dp_now = [0] + [1] * 10 + [0]
dp_nxt = [0] * 12
for n in range(1, N):
    for i in range(1, 11):
        dp_nxt[i] = (dp_now[i - 1] + dp_now[i + 1]) % 1000000000
    dp_now = dp_nxt
    dp_nxt = [0] * 12
print(sum(dp_now[2:11]) % 1000000000)