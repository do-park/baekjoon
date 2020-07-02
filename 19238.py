# BOJ 19238 스타트 택시

from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def get_customer():
    visited = [[400] * N for _ in range(N)]
    q = deque()
    visited[sy][sx] = 0
    q.append([sy, sx])
    while q:
        y, x = q.popleft()
        next = visited[y][x] + 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not maps[ny][nx] and next < visited[ny][nx]:
                visited[ny][nx] = next
                q.append([ny, nx])
    customer = -1
    distance = 400
    for c in range(len(customers)):
        if visited[customers[c][0]][customers[c][1]] < distance:
            customer = c
            distance = visited[customers[c][0]][customers[c][1]]
    return customer, distance


def move_customer(c):
    visited = [[400] * N for _ in range(N)]
    q = deque()
    visited[c[0]][c[1]] = 0
    q.append([c[0], c[1]])
    while q:
        y, x = q.popleft()
        next = visited[y][x] + 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not maps[ny][nx] and next < visited[ny][nx]:
                visited[ny][nx] = next
                q.append([ny, nx])
    return visited[c[2]][c[3]]


N, M, G = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1
customers = [list(map(int, input().split())) for _ in range(M)]
for m in range(M):
    customers[m][0], customers[m][1], customers[m][2], customers[m][3] = customers[m][0] - 1, customers[m][1] - 1, customers[m][2] - 1, customers[m][3] - 1
customers.sort(key=lambda x: (x[0], x[1]))
for m in range(M):
    customer, distance = get_customer()
    if distance >= G or distance == 400:
        print(-1)
        break
    G -= distance
    distance = move_customer(customers[customer])
    if distance > G or distance == 400:
        print(-1)
        break
    G = G + distance
    sy, sx = customers[customer][2], customers[customer][3]
    customers.pop(customer)
else:
    print(G)