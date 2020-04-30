# BOJ 1929 소수 구하기

def primenum(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

M, N = map(int, input().split())
for i in range(M, N + 1):
    if primenum(i):
        print(i)