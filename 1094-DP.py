# BOJ 1094 막대기 - 다이나믹 프로그래밍

result = [100] * 65
temp = 64
while temp > 0:
    result[temp] = 1
    temp //= 2
X = int(input())
for i in range(3, X + 1):
    if result[i] == 100:
        for j in range(1, i):
            result[i] = min(result[i], result[j] + result[i - j])
print(result[X])