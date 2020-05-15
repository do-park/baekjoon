# BOJ 2473 세 용액
# 시간 초과

N = int(input())
liquid = sorted(list(map(int, input().split())))
answer = 3000000000
answer1, answer2, answer3 = 0, 0, 0
for i in range(N - 2):
    start, end = i + 1, N - 1
    temp = liquid[i] + liquid[start] + liquid[end]
    while start < end:
        if abs(temp) < abs(answer):
            answer = temp
            answer1, answer2, answer3 = liquid[i], liquid[start], liquid[end]
            if temp == 0:
                break
        if temp > 0:
            temp -= liquid[end]
            end -= 1
            temp += liquid[end]
        elif temp < 0:
            temp -= liquid[start]
            start += 1
            temp += liquid[start]
print(answer1, answer2, answer3)