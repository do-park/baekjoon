# BOJ 16234 인구 이동

from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0
while True:
    NN = N * N
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                NN -= 1
                Alist = [[i, j]]
                Q.append([i, j, A[i][j]])
                visited[i][j] = 1
                total = A[i][j]
                count = 1
                while Q:
                    y, x, population = Q.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(population - A[ny][nx]) <= R:
                            Q.append([ny, nx, A[ny][nx]])
                            visited[ny][nx] = 1
                            total += A[ny][nx]
                            count += 1
                            Alist.append([ny, nx])
                for a in Alist:
                    new_pop = total // count
                    A[a[0]][a[1]] = new_pop
    if not NN:
        break
    result += 1
print(result)