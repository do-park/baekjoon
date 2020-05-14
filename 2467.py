# BOJ 2467 용액

N = int(input())
A = sorted(list(map(int, input().split())))
answer = 2000000000
answer1, answer2 = 0, 0
start, end = 0, N - 1
while start < end:
    result = A[start] + A[end]
    if abs(result) < abs(answer):
        answer = result
        answer1, answer2 = A[start], A[end]
        if result == 0:
            break
    if result < 0:
        start += 1
    elif result > 0:
        end -= 1
print(answer1, answer2)