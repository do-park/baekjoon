# BOJ 13458 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0
for n in range(N):
    A[n] = max(A[n] - B, 0)
    count += 1
    if A[n]:
        count += A[n] // C
        if A[n] % C:
            count += 1
print(count)