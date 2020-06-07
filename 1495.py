# BOJ 1495 메모리 초과

from collections import deque

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[] for _ in range(N + 1)]
dp[0].append(S)
q = deque()
q.append([S, 0])
while q:
    volume, idx = q.popleft()
    if idx < N:
        if 0 <= volume - V[idx]:
            nxt = volume - V[idx]
            dp[idx + 1].append(nxt)
            q.append([nxt, idx + 1])
        if volume + V[idx] <= M:
            nxt = volume + V[idx]
            dp[idx + 1].append(nxt)
            q.append([nxt, idx + 1])
print(max(dp[-1]) if dp[-1] else -1)