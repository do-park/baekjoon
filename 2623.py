# BOJ 2623 음악프로그램

from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for m in range(M):
    pd = list(map(int, input().split()))
    for n in range(2, len(pd)):
        indegree[pd[n]] += 1
        graph[pd[n - 1]].append(pd[n])
q = deque()
for n in range(1, N + 1):
    if not indegree[n]:
        q.append(n)
result = []
while q:
    singer = q.popleft()
    result.append(singer)
    for i in graph[singer]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)
if len(result) != N:
    print(0)
else:
    for n in range(N):
        print(result[n])