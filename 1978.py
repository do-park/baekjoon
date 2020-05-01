# BOJ 1978 소수 찾기

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
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
prime = []
for i in range(1, numbers[0] + 1):
    if is_prime(i):
        prime.append(i)
count = 0
for i in numbers:
    if i in prime:
        count += 1
print(count)