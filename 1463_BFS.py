# BOJ 1463 1로 만들기

from collections import deque

N = int(input())
visited = [0] * 1000001
q = deque()
q.append([1, 0])
while q:
    pos, cost = q.popleft()
    if pos == N:
        break
    c = cost + 1
    for p in [pos + 1, pos * 2, pos * 3]:
        if p > 1000000:
            continue
        if visited[p]:
            continue
        visited[p] = c
        q.append([p, c])
print(visited[N])