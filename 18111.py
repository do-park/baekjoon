# BOJ 18111 마인크래프트

N, M, B = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
mini, maxi = 257, -1
blocks = [0] * 257
for n in range(N):
    for m in range(M):
        if maps[n][m] < mini:
            mini = maps[n][m]
        if maps[n][m] > maxi:
            maxi = maps[n][m]
        blocks[maps[n][m]] += 1
time, height = 987654321, 0
for h in range(mini, maxi + 1):
    low, high = 0, 0
    for i in range(257):
        if i < h:
            low += (h - i) * blocks[i]
        elif i > h:
            high += (i - h) * blocks[i]
    if low <= high + B:
        t = low + high * 2
        if t <= time:
            time = t
            height = h
print(time, height)