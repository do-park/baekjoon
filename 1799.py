# BOJ 1799 비숍
# 시간 초과

def bishop(start=0, count=0):
    global result
    for i in range(start, end):
        y = i // N
        x = i % N
        if maps[y][x] and (y - x) not in dgnl1 and (y + x) not in dgnl2:
            dgnl1.append(y - x)
            dgnl2.append(y + x)
            bishop(i + 1, count + 1)
            dgnl1.pop()
            dgnl2.pop()
    if count > result:
        result = count
    return

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dgnl1 = []  # y - x
dgnl2 = []  # y + x
end = N * N
result = 0
bishop()
print(result)