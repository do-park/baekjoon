# BOJ 2252 줄 세우기

from collections import deque

N, M = map(int, input().split())
height = []
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
q = deque()
for m in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
for n in range(1, N + 1):
    if not indegree[n]:
        q.append(n)
result = []
while q:
    student = q.popleft()
    result.append(student)
    for i in graph[student]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)
print(*result)