# BOJ 2473 세 용액

N = int(input())
liquid = sorted(list(map(int, input().split())))
answer = 3000000000
answer1, answer2, answer3 = 0, 0, 0
flag = 0
for i in range(N - 2):
    st, en = i + 1, N - 1
    while st < en:
        temp = liquid[i] + liquid[st] + liquid[en]
        if abs(temp) < answer:
            answer = abs(temp)
            answer1, answer2, answer3 = liquid[i], liquid[st], liquid[en]
            if temp == 0:
                flag = 1
                break
        if temp > 0:
            en -= 1
        elif temp < 0:
            st += 1
    if flag:
        break
print(answer1, answer2, answer3)