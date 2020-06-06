# BOJ 1932 정수 삼각형

N = int(input())
dp_now = [0] * (N + 1)
dp_nxt = [0] * (N + 1)
for n in range(N):
    temp = [0] + list(map(int, input().split()))
    for i in range(1, len(temp)):
        dp_nxt[i] = max(dp_now[i - 1], dp_now[i]) + temp[i]
    dp_now = dp_nxt
    dp_nxt = [0] * (N + 1)
print(max(dp_now))