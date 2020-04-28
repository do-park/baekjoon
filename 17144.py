# BOJ 17144 미세먼지 안녕!

def spread(now):
    next = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if now[y][x] == -1:
                next[y][x] = -1
            else:
                if now[y][x] != 0:
                    count = 0
                    dust = now[y][x] // 5
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < R and 0 <= nx < C and now[ny][nx] != -1:
                            next[ny][nx] += dust
                            count += 1
                    next[y][x] = next[y][x] + now[y][x] - dust * count
    return next

def purify(now):
    # 상단은 반시계 방향
    for i in range(purifier[0] - 1, 0, -1):
        now[i][0] = now[i - 1][0]
    for i in range(0, C - 1):
        now[0][i] = now[0][i + 1]
    for i in range(purifier[0]):
        now[i][C - 1] = now[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        now[purifier[0]][i] = now[purifier[0]][i - 1]
    now[purifier[0]][1] = 0
    # 하단은 시계 방향
    for i in range(purifier[1] + 1, R - 1):
        now[i][0] = now[i + 1][0]
    for i in range(C - 1):
        now[R - 1][i] = now[R - 1][i + 1]
    for i in range(R - 1, purifier[1], -1):
        now[i][C - 1] = now[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        now[purifier[1]][i] = now[purifier[1]][i - 1]
    now[purifier[1]][1] = 0


R, C, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
purifier = []
for i in range(2, R):
    if maps[i][0] == -1:
        purifier.append(i)
        purifier.append(i + 1)
        break
for t in range(T):
    maps = spread(maps)
    purify(maps)
result = 2
for i in range(R):
    result += sum(maps[i])
print(result)