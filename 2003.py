# BOJ 2003 수들의 합 2

N, M = map(int, input().split())
A = list(map(int, input().split()))
start, end, total, count = 0, 0, 0, 0
while True:
    if total >= M:
        total -= A[start]
        start += 1
    elif end == N:
        break
    else:
        total += A[end]
        end += 1
    if total == M:
        count += 1
print(count)