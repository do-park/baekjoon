# BOJ 17090 미로 탈출하기

from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()
i = 1
escape = []
result = 0
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            visited[n][m] = i
            q.append([n, m])
            count = 1
            while q:
                y, x = q.popleft()
                if maps[y][x] == 'U':
                    ny, nx = y - 1, x
                elif maps[y][x] == 'D':
                    ny, nx = y + 1, x
                elif maps[y][x] == 'L':
                    ny, nx = y, x - 1
                elif maps[y][x] == 'R':
                    ny, nx = y, x + 1
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx]:
                        visited[ny][nx] = i
                        q.append([ny, nx])
                        count += 1
                    elif visited[ny][nx] in escape:
                        escape.append(i)
                        result += count
                    elif visited[ny][nx] == i:
                        break
                else:
                    escape.append(i)
                    result += count
            i += 1
print(result)