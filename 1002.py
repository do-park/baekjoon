# BOJ 1002 터렛

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R = r1 + r2
    R = R ** 2
    r = abs(r1 - r2)
    r = r ** 2
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if r < d < R:
        print(2)
    elif d == R or (d == r and d != 0):
        print(1)
    elif d < r or d > R:
        print(0)
    elif d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)