# BOJ 2470 두 용액

N = int(input())
liquid = sorted(list(map(int, input().split())))
start, end = 0, N - 1
answer = 2000000000
answer1, answer2 = 0, 0
while start < end:
    temp = liquid[start] + liquid[end]
    if abs(temp) < abs(answer):
        answer = temp
        answer1 = liquid[start]
        answer2 = liquid[end]
        if temp == 0:
            break
    if temp > 0:
        end -= 1
    elif temp < 0:
        start += 1
print(answer1, answer2)