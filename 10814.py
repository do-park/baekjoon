# BOJ 10814 나이순 정렬

N = int(input())
user = []
for n in range(N):
    age, name = input().split()
    user.append([n, int(age), name])
result = sorted(user, key=lambda x: (x[1], x[0]))
for n in range(N):
    print(result[n][1], result[n][2])