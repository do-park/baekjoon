# BOJ 16929 Two Dots
from collections import deque

N, M = map(int, input().split())
maps = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = deque()
count = 1
flag = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            color = maps[n][m]
            visited[n][m] = count
            Q.append([n, m, n, m])
            while Q:
                y, x, by, bx = Q.popleft()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == color:
                        if not visited[ny][nx]:
                            visited[ny][nx] = count
                            Q.append([ny, nx, y, x])
                        else:
                            if ny != by and nx != bx:
                                flag = 1
                                Q = deque()
                                break
            count += 1
            if flag: break
        if flag: break
    if flag: break
if flag: print('Yes')
else: print('No')