# BOJ 2665 미로만들기

from collections import deque
INF = 1e9

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[INF] * N for _ in range(N)]
q = deque()
visited[0][0] = 0
q.append([0, 0])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while q:
    y, x = q.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > visited[y][x] + (1 - maps[ny][nx]):
            visited[ny][nx] = visited[y][x] + (1 - maps[ny][nx])
            k = visited[ny][nx]
            q.append([ny, nx])
print(visited[N - 1][N - 1])