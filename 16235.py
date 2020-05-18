# BOJ 16235 나무재테크

from collections import deque

N, M, K = map(int, input().split())
maps = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]
trees = {(i, j): deque() for i in range(N) for j in range(N)}
for m in range(M):
    x, y, z = map(int, input().split())
    trees[(x - 1, y - 1)].append(z)
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
for k in range(K):
    for (x, y), tree in trees.items():
        temp = deque()
        nutrient = 0
        for t in tree:
            if maps[x][y] >= t:
                maps[x][y] -= t
                temp.append(t + 1)
            else:
                nutrient += t // 2
        trees[(x, y)] = temp
        maps[x][y] += nutrient
    for (x, y), tree in trees.items():
        for t in tree:
            if t % 5 == 0:
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        trees[(nx, ny)].appendleft(1)
    for i in range(N):
        for j in range(N):
            maps[i][j] += s2d2[i][j]
result = 0
for (x, y), tree in trees.items():
    result += len(tree)
print(result)