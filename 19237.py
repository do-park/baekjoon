# BOJ 19237 어른 상어

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
N, M, K = map(int, input().split())
sharks = [[-1, -1] for _ in range(M + 1)]
odor = [[0 for _ in range(N)] for _ in range(N)]
maps = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if maps[i][j]:
            odor[i][j] = [K, maps[i][j]]
            sharks[maps[i][j]] = [i, j]
shark_dir = [0] + list(map(int, input().split()))
move_priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
time = 0
S = M
while S > 1 and time < 1001:
    for m in range(1, M + 1):
        if sharks[m][0] > -1:
            y, x = sharks[m][0], sharks[m][1]
            dir = move_priority[m - 1][shark_dir[m] - 1]
            for d in dir:
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < N and not odor[ny][nx]:
                    if not maps[ny][nx]:
                        sharks[m][0], sharks[m][1] = ny, nx
                        maps[y][x], maps[ny][nx] = 0, m
                        shark_dir[m] = d
                        break
                    else:
                        sharks[m][0], sharks[m][1] = -1, -1
                        maps[y][x] = 0
                        S -= 1
                        break
            else:
                for d in dir:
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if odor[ny][nx][1] == m:
                            sharks[m][0], sharks[m][1] = ny, nx
                            maps[y][x], maps[ny][nx] = 0, m
                            shark_dir[m] = d
                            break
    for i in range(N):
        for j in range(N):
            if odor[i][j]:
                if odor[i][j][0] == 1:
                    odor[i][j] = 0
                else:
                    odor[i][j][0] -= 1
    for m in range(1, M + 1):
        if sharks[m][0] > -1:
            odor[sharks[m][0]][sharks[m][1]] = [K, m]
    time += 1
print(time if time < 1001 else -1)