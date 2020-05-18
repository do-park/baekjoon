# BOJ 6593 상범 빌딩

from collections import deque

while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    building = [[[] * C for _ in range(R)] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    for l in range(L):
        building[l] = [list(map(str, input())) for _ in range(R)]
        input()
    q = deque()
    E = [0, 0, 0]
    flag = 0
    for l in range(L):
        if flag == 2:
            break
        for r in range(R):
            if flag == 2:
                break
            for c in range(C):
                if building[l][r][c] == 'S':
                    q.append([l, r, c])
                    visited[l][r][c] = 1
                    flag += 1
                if building[l][r][c] == 'E':
                    E[0], E[1], E[2] = l, r, c
                    flag += 1
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]
    while q:
        z, y, x = q.popleft()
        for d in range(6):
            nz, ny, nx = z + dz[d], y + dy[d], x + dx[d]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and building[nz][ny][nx] != '#' and (not visited[nz][ny][nx] or visited[nz][ny][nx] > visited[z][y][x] + 1):
                q.append([nz, ny, nx])
                visited[nz][ny][nx] = visited[z][y][x] + 1
    if visited[E[0]][E[1]][E[2]]:
        print(f'Escaped in {visited[E[0]][E[1]][E[2]] - 1} minute(s)')
    else:
        print('Trapped!')