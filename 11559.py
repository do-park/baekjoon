# BOJ 11559 Puyo Puyo
# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 문장부터 처리


from collections import deque

Y = 12
X = 6
maps = [list(map(str, input())) for _ in range(Y)]
visited = [[False] * X for _ in range(Y)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque()
result = 0
flag = 1
while flag:
    for i in range(Y):
        for j in range(X):
            visited[i][j] = True
            if maps[i][j] != '.':
                std = maps[i][j]
                Q.append([i, j])
                count = 1
                yxs = [[i, j]]
                while Q:
                    y, x = Q.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and maps[ny][nx] == std:
                            visited[ny][nx] = True
                            Q.append([ny, nx])
                            count += 1
                            yxs.append([ny, nx])
                if count > 3:
                    result += 1
                    for c in range(count):
                        print(yxs)
                        maps[yxs[c][0]][yxs[c][1]] = '.'
                        print(maps)
                print(maps)