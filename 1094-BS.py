# BOJ 1094 막대기 - 이분탐색

X = int(input())
right = 64
left = 0
result = 0
if X == 64:
    print(result + 1)
else:
    while left < right:
        mid = (left + right) // 2
        if X == mid:
            print(result + 1)
            break
        elif X < mid:
            right = mid
        else:
            left = mid
            result += 1