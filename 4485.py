# BOJ 4485 녹색 옷 입은 애가 젤다지?

from collections import deque

INF = 1e9
tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    q = deque()
    visited[0][0] = maps[0][0]
    q.append([0, 0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > visited[y][x] + maps[ny][nx]:
                visited[ny][nx] = visited[y][x] + maps[ny][nx]
                q.append([ny, nx])
    print(f'Problem {tc}: {visited[N - 1][N - 1]}')
    tc += 1