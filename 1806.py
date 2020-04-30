# BOJ 1806 부분합

import sys
N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = N + 1
start, end, total = 0, 0, 0
while True:
    if total >= S:
        result = min(end - start, result)
        total -= numbers[start]
        start += 1
    elif end == N:
        break
    else:
        total += numbers[end]
        end += 1
if result == N + 1:
    print(0)
else:
    print(result)