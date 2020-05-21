# BOJ 15683 감시

def func(i=0):
    global result
    if C == i:
        count = 0
        for n in range(N):
            for m in range(M):
                if not maps[n][m]:
                    count += 1
        result = min(result, count)
        return
    y, x, c = cctv[i]
    for chk in check[c]:
        watch = []
        for d in chk:
            ny, nx = y, x
            while 0 <= ny < N and 0 <= nx < M and maps[ny][nx] != 6:
                if maps[ny][nx] == 0:
                    watch.append([ny, nx])
                    maps[ny][nx] = -1
                ny += dy[d]
                nx += dx[d]
        func(i + 1)
        for w in watch:
            maps[w[0]][w[1]] = 0


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
check = [[[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]
cctv = []
for n in range(N):
    for m in range(M):
        if maps[n][m] != 0 and maps[n][m] != 6:
            cctv.append((n, m, maps[n][m] - 1))
cctv = sorted(cctv, key=lambda x:(-x[2]))
C = len(cctv)
result = N * M
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
func()
print(result)