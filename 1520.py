# BOJ 1520 내리막길
# 메모리 초과

from collections import deque

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
q = deque()
dp[0][0] = 1
q.append([0, 0])
while q:
    y, x = q.popleft()
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < M and 0 <= nx < N and maps[ny][nx] < maps[y][x]:
            dp[ny][nx] += 1
            q.append([ny, nx])
print(dp[-1][-1])