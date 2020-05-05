# BOJ 11559 Puyo Puyo

from collections import deque

Y = 12
X = 6
maps = [list(map(str, input())) for _ in range(Y)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque()
result = 0
while True:
    flag = False
    visited = [[False] * X for _ in range(Y)]
    for i in range(Y):
        for j in range(X):
            visited[i][j] = True
            if maps[i][j] != '.':
                color = maps[i][j]
                Q.append([i, j])
                count = 1
                yxs = [[i, j]]
                while Q:
                    y, x = Q.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < Y and 0 <= nx < X and not visited[ny][nx] and maps[ny][nx] == color:
                            visited[ny][nx] = True
                            Q.append([ny, nx])
                            count += 1
                            yxs.append([ny, nx])
                if count > 3:
                    flag = True
                    for c in range(count):
                        maps[yxs[c][0]][yxs[c][1]] = '.'
    if not flag:
        break
    result += 1
    for x in range(X):
        for y in range(Y - 1, -1, -1):
            if maps[y][x] == '.':
                continue
            for r in range(Y - 1, y, -1):
                if maps[r][x] == '.':
                    maps[r][x] = maps[y][x]
                    maps[y][x] = '.'
print(result)