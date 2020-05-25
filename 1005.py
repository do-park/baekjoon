# BOJ 1005 ACM Craft
# 시간 초과

import sys

def find(x):
    if parent[x]:
        temps = []
        for y in parent[x]:
            temp = find(y)
            temps.append(temp)
        return max(temps) + D[x - 1]
    else:
        return D[x - 1]

for tc in range(1, int(sys.stdin.readline()) + 1):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    parent = [[] for _ in range(N + 1)]
    for k in range(K):
        x, y = map(int, input().split())
        parent[y].append(x)
    W = int(input())
    print(find(W))