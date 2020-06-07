# BOJ 11054 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int, input().split()))
dpF = [0] * N
dpR = [0] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dpF[i] = max(dpF[i], dpF[j] + 1)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            dpR[i] = max(dpR[i], dpR[j] + 1)
result = 0
for n in range(N):
    temp = dpF[n] + dpR[n]
    if result < temp:
        result = temp
print(result + 1)