# BOJ 1806 부분합
# 시간 초과 (3%)
# two-pointer 개념

import sys
N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = N + 1
for start in range(N):
    total = 0
    for end in range(start, N):
        total += numbers[end]
        if total >= S and end - start < result:
            result = end - start
            break
if result == N + 1:
    print(0)
else:
    print(result + 1)