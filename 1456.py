# BOJ 1456 거의 소수
# 시간 초과

def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


A, B = map(int, input().split())
prime = []
for i in range(A, B + 1):
    if is_prime(i):
        prime.append(i)
count = 0
for p in range(len(prime)):
    i = 2
    while True:
        if prime[p] ** i < B:
            count += 1
            i += 1
        else:
            break
print(count)