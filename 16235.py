# BOJ 16235 나무재테크
# T/O 나올 것 같아 제출은 하지 않음

N, M, K = map(int, input().split())
maps = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]
for tree in trees:
    tree[0], tree[1] = tree[0] - 1, tree[1] - 1
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
for k in range(K):
    trees = sorted(trees, key=lambda x: (x[2]))
    deads = []
    # 봄
    for tree in trees:
        x, y, z = tree
        if maps[y][x] >= z:
            maps[y][x] -= z
            tree[2] += 1
        else:
            deads.append(tree)
    # 여름
    for dead in deads:
        x, y, z = dead
        maps[y][x] += z // 2
        trees.remove(dead)
    # 가을
    for tree in trees:
        if tree[2] % 5 == 0:
            # 8개 방향에 나이 1의 나무 8그루 심기
            x, y, z = tree
            for d in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    trees.append([nx, ny, 1])
    # 겨울
    for i in range(N):
        for j in range(N):
            maps[i][j] += s2d2[i][j]
print(len(trees))