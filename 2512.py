# BOJ 2512 예산

N = int(input())
budget = list(map(int, input().split()))
M = int(input())
if sum(budget) <= M:
    print(max(budget))
else:
    total = 0
    limit = 0
    st = 0
    en = max(budget)
    while st <= en:
        md = (st + en) // 2
        result = 0
        for n in range(N):
            if budget[n] < md:
                result += budget[n]
            else:
                result += md
        if total < result <= M:
            total = result
            limit = md
        if result == M:
            break
        elif result < M:
            st = md + 1
        else:
            en = md - 1
    print(limit)