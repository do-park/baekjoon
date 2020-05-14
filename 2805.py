# BOJ 2805 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))
low, high = 0, max(trees)
answer = 0
while low <= high:
    mid = (low + high) // 2
    result = 0
    for tree in trees:
        result += max(tree - mid, 0)
    if result == M:
        answer = mid
        break
    elif result < M:
        high = mid - 1
    elif result > M:
        low = mid + 1
        answer = mid
print(answer)