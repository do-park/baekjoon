# BOJ 3190 뱀
# 주어진 명령어 마친 뒤의 움직임을 어떻게 표현할 것인가
from collections import deque

N = int(input())
K = int(input())
maps = [[0] * N for _ in range(N)]
snake = deque()
snake.append([0, 0])
D = 1
time = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for k in range(K):
    y, x = map(int, input().split())
    maps[y - 1][x - 1] = 1
L = int(input())
flag = 1
for l in range(L):
    t, d = input().split()
    t = int(t)
    # 뱀 움직이기
    while flag and time < t:
        ny = snake[0][0] + dy[D]
        nx = snake[0][1] + dx[D]
        if 0 <= ny < N and 0 <= nx < N and [ny, nx] not in snake:
            if maps[ny][nx]:
                snake.appendleft([ny, nx])
                maps[ny][nx] = 0
            else:
                snake.appendleft([ny, nx])
                snake.pop()
            print(snake)
        else:
            print('==GAME OVER==')
            print(time)
            flag = 0
        time += 1
        if time == t:
            if d == 'L':
                D = D - 1 if D > 0 else 3
            else:
                D = (D + 1) % 4
            print(time, D)
print(time)