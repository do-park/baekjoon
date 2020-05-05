# BOJ 11559 Puyo Puyo

from collections import deque

maps = [list(map(str, input())) for _ in range(12)]
new = [[maps[m][n] for m in reversed(range(12))] for n in range(6)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0
while True:
    puyo = []
    Q = deque()
    visited = [[False] * 12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if new[i][j] != '.' and not visited[i][j]:
                color = new[i][j]
                Q.append([i, j])
                visited[i][j] = True
                temp = [[i, j]]
                count = 1
                while Q:
                    y, x = Q.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < 6 and 0 <= nx < 12 and new[ny][nx] == color and not visited[ny][nx]:
                            Q.append([ny, nx])
                            visited[ny][nx] = True
                            temp.append([ny, nx])
                            count += 1
                if count > 3:
                    puyo += temp
    if not puyo:
        break
    puyo = sorted(puyo, key=lambda x: (-x[0], -x[1]))
    for y, x in puyo:
        new[y].pop(x)
    for i in range(6):
        new[i] = new[i] + ['.'] * (12 - len(new[i]))
    result += 1
print(result)