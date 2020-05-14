# BOJ 14921 용액 합성하기

N = int(input())
A = sorted(list(map(int,input().split())))
start, end = 0, N - 1
answer = 200000000
while start < end:
    result = A[start] + A[end]
    if abs(result) < abs(answer):
        answer = result
        if answer == 0:
            break
    if result > 0:
        end -= 1
    if result < 0:
        start += 1
print(answer)