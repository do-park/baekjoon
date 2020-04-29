# BOJ 16236 아기 상어

from collections import deque

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
shark = 2
Q = deque()
visited = [[400] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            Q.append([i, j])
            visited[i][j] = 0
            maps[i][j] = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0
eat = 0
while True:
    temp = []
    dist = 400
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] <= shark and visited[ny][nx] > visited[y][x] + 1:
                Q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                if maps[ny][nx] < shark:
                    if maps[ny][nx]:
                        if dist > visited[ny][nx]:
                            dist = visited[ny][nx]
                            temp = [[ny, nx]]
                        elif dist == visited[ny][nx]:
                            temp.append([ny, nx])
    if not temp: break
    visited = [[400] * N for _ in range(N)]
    result = sorted(temp, key=lambda r: (r[0], r[1]))
    Q.append(result[0])
    visited[result[0][0]][result[0][1]] = 0
    maps[result[0][0]][result[0][1]] = 0
    answer += dist
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0
print(answer)