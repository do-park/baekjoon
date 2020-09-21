# BOJ 1094 막대기 - 시뮬레이션

X = int(input())
stick = 64
result = 0
while X > 0:
    if X >= stick:
        result += 1
        X -= stick
    else:
        stick //= 2
print(result)