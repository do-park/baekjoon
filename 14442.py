# BOJ 14442 벽 부수고 이동하기 2

from collections import deque


def bfs():
    Q = deque()
    Q.append([K, 0, 0])
    visited[K][0][0] = 1
    while Q:
        k, y, x = Q.popleft()
        if y == N - 1 and x == M - 1:
            return visited[k][y][x]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if maps[ny][nx] == 0 and (visited[k][ny][nx] == 0 or visited[k][ny][nx] > visited[k][y][x] + 1):
                    Q.append([k, ny, nx])
                    visited[k][ny][nx] = visited[k][y][x] + 1
                elif maps[ny][nx] == 1 and k > 0 and (visited[k - 1][ny][nx] == 0 or visited[k - 1][ny][nx] > visited[k][y][x] + 1):
                    Q.append([k - 1, ny, nx])
                    visited[k - 1][ny][nx] = visited[k][y][x] + 1
    return -1


N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
print(bfs())