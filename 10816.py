# BOJ 10816 숫자 카드 2

def upper_bound(arr, target, size):
    start, end = 0, size
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end

def lower_bound(arr, target, size):
    start, end = 0, size
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for number in B:
    U = upper_bound(A, number, N)
    L = lower_bound(A, number, N)
    if U == L:
        if A[U - 1] == number:
            print(1, end=' ')
        else:
            print(0, end=' ')
    else:
        print(U - L, end=' ')