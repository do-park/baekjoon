# BOJ 17136 색종이 붙이기

def check(y, x, k):
    for i in range(y, y + k):
        for j in range(x, x + k):
            if i > 9 or j > 9:
                return False
            if visited[i][j] or not maps[i][j]:
                return False
    return True

def func(res=0, done=0):
    global result
    if len(spaces) == done:
        result = min(result, res)
        return
    if res > result:
        return
    for i in range(len(spaces)):
        y, x = spaces[i][0], spaces[i][1]
        if visited[y][x]:
            continue
        for j in range(5, 0, -1):
            if not papers[j]:
                continue
            if check(y, x, j):
                for a in range(y, y + j):
                    for b in range(x, x + j):
                        visited[a][b] = True
                papers[j] -= 1
                func(res + 1, done + (j * j))
                for a in range(y, y + j):
                    for b in range(x, x + j):
                        visited[a][b] = False
                papers[j] += 1
        return





spaces = []
maps = []
for i in range(10):
    temp = list(map(int, input().split()))
    maps.append(temp)
    for j in range(10):
        if temp[j]:
            spaces.append([i, j])
visited = [[False] * 10 for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
result = 26
func()
if result > 25:
    print(-1)
else:
    print(result)