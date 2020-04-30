# BOJ 1644 소수의 연속합

def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


N = int(input())
prime = []
for i in range(2, N + 1):
    if is_prime(i):
        prime.append(i)
start, end, total, count = 0, 0, 0, 0
while True:
    if total >= N:
        total -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        total += prime[end]
        end += 1
    if total == N:
        count += 1
print(count)