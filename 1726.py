# BOJ 1726 로봇

from collections import deque
dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]
M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
visited = [[[1000] * N for _ in range(M)] for _ in range(5)]
sy, sx, sd = map(int, input().split())
sy, sx, = sy - 1, sx - 1
visited[sd][sy][sx] = 0
q = deque()
q.append([sy, sx, sd])
ey, ex, ed = map(int, input().split())
ey, ex = ey - 1, ex - 1
while q:
    y, x, d = q.popleft()
    next = visited[d][y][x] + 1
    for i in range(1, 4):
        ny, nx = y + (dy[d] * i), x + (dx[d] * i)
        if 0 <= ny < M and 0 <= nx < N and maps[ny][nx] == 0 and next <= visited[d][ny][nx]:
            visited[d][ny][nx] = next
            q.append([ny, nx, d])
        else:
            break
    if d < 3:
        if visited[3][y][x] > next:
            visited[3][y][x] = next
            q.append([y, x, 3])
        if visited[4][y][x] > next:
            visited[4][y][x] = next
            q.append([y, x, 4])
    else:
        if visited[1][y][x] > next:
            visited[1][y][x] = next
            q.append([y, x, 1])
        if visited[2][y][x] > next:
            visited[2][y][x] = next
            q.append([y, x, 2])
print(visited[ed][ey][ex])