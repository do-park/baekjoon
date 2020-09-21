# BJ 13460 구슬탈출 2

from collections import deque
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


N, M = map(int, input().split())
maps = [list(map(str, input())) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = deque()
for n in range(N):
    for m in range(M):
        if maps[n][m] == 'R':
            ry, rx = n, m
        elif maps[n][m] == 'B':
            by, bx = n, m

def move(y, x, dy, dx):
    cnt = 0
    while maps[y+dy][x+dx] != '#' and maps[y][x] != 'O':
        y, x = y + dy, x + dx
        cnt += 1
    return y, x, cnt

visited[ry][rx][by][bx] = True
q.append((ry, rx, by, bx, 0))
flag = True
while q and flag:
    ry, rx, by, bx, depth = q.popleft()
    if depth == 10:
        break
    depth += 1
    for dy, dx in DELTAS:
        nry, nrx, rcnt = move(ry, rx, dy, dx)
        nby, nbx, bcnt = move(by, bx, dy, dx)
        if maps[nby][nbx] == 'O':
            continue
        if maps[nry][nrx] == 'O':
            flag = False
            break
        if nry == nby and nrx == nbx:
            if rcnt > bcnt:
                nry, nrx = nry - dy, nrx - dx
            else:
                nby, nbx = nby - dy, nbx - dx
        if not visited[nry][nrx][nby][nbx]:
            visited[nry][nrx][nby][nbx] = True
            q.append((nry, nrx, nby, nbx, depth))
print(-1 if flag else depth)