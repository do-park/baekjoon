# BOJ 14503 로봇 청소기

N, M = map(int, input().split())
y, x, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[y][x] = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
count = 0
while True:
    nd = d - 1 if d > 0 else 3
    ny = y + dy[nd]
    nx = x + dx[nd]
    if 0 <= ny < N and 0 <= nx < M and not maps[ny][nx] and not visited[ny][nx]:
        visited[ny][nx] = visited[y][x] + 1
        y, x, d = ny, nx, nd
        count = 0
    else:
        d = nd
        count += 1
        if count > 4:
            bd = d - 1 if d > 0 else 3
            by = y + dy[bd]
            bx = x + dx[bd]
            if 0 <= by < N and 0 <= bx < M and not maps[by][bx]:
                visited[by][bx] = visited[y][x]
                y, x, d = by, bx, bd + 2 if bd < 2 else bd - 2
                count = 0
            else:
                break
print(visited[y][x])