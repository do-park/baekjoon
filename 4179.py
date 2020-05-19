# BOJ 4179 불!

from collections import deque

def bfs(q, fq):
    tq = deque()
    while q:
        while fq:
            y, x = fq.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and (maps[ny][nx] == '.' or maps[ny][nx] == 'J'):
                    maps[ny][nx] = 'F'
                    tq.append([ny, nx])
        fq = tq
        tq = deque()
        while q:
            y, x = q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < R and 0 <= nx < C:
                    if maps[ny][nx] == '.':
                        maps[ny][nx] = 'J'
                        tq.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1
                else:
                    print(visited[y][x])
                    return
        q = tq
        tq = deque()
        # for i in range(R):
        #     print(maps[i])
        # print()
    print('IMPOSSIBLE')
    return


R, C = map(int, input().split())
maps = [list(map(str, input())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
q = deque()
fq = deque()
for r in range(R):
    for c in range(C):
        if maps[r][c] == 'J':
            q.append([r, c])
            visited[r][c] = 1
        if maps[r][c] == 'F':
            fq.append([r, c])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
bfs(q, fq)