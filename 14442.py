# BOJ 14442 벽 부수고 이동하기 2
# 98% 에서 틀렸습니다.

from collections import deque

N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[N * M] * M for _ in range(N)] for _ in range(K + 1)]
Q = deque()
Q.append([K, 0, 0])
visited[K][0][0] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while Q:
    k, y, x = Q.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if maps[ny][nx] == 0 and visited[k][ny][nx] > visited[k][y][x] + 1:
                Q.append([k, ny, nx])
                visited[k][ny][nx] = visited[k][y][x] + 1
            elif maps[ny][nx] == 1 and k and visited[k - 1][ny][nx] > visited[k][y][x] + 1:
                Q.append([k - 1, ny, nx])
                visited[k - 1][ny][nx] = visited[k][y][x] + 1
result = visited[K][N - 1][M - 1]
for k in range(K):
    result = min(result, visited[k][N - 1][M - 1])
if result == M * N:
    print(-1)
else:
    print(result)
print(visited)