# BOJ 2096 내려가기

N = int(input())
score = list(map(int, input().split()))
dp_min = score
dp_max = score
temp_min = [0, 0, 0]
temp_max = [0, 0, 0]
for n in range(N - 1):
    score = list(map(int, input().split()))
    temp_min[0] = score[0] + min(dp_min[0], dp_min[1])
    temp_min[1] = score[1] + min(dp_min)
    temp_min[2] = score[2] + min(dp_min[1], dp_min[2])
    temp_max[0] = score[0] + max(dp_max[0], dp_max[1])
    temp_max[1] = score[1] + max(dp_max)
    temp_max[2] = score[2] + max(dp_max[1], dp_max[2])
    dp_min = temp_min
    dp_max = temp_max
    temp_min = [0, 0, 0]
    temp_max = [0, 0, 0]
print(f'{max(dp_max)} {min(dp_min)}')