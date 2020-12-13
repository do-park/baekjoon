# 백준 1072 게임

X, Y = map(int, input().split())
Z = 100 * Y // X + 1
left, right = 1, X
if Z > 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        newZ = 100 * (Y + mid) // (X + mid)
        if newZ >= Z:
            right = mid - 1
        else:
            left = mid + 1
    print(left)