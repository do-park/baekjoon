# BOJ 2096 내려가기
# 메모리 초과

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
dp_min = [[0, 0, 0] for _ in range(N)]
dp_max = [[0, 0, 0] for _ in range(N)]
dp_min[0][0] = dp_max[0][0] = score[0][0]
dp_min[0][1] = dp_max[0][1] = score[0][1]
dp_min[0][2] = dp_max[0][2] = score[0][2]
for n in range(1, N):
    dp_min[n][0] = score[n][0] + min(dp_min[n - 1][0], dp_min[n - 1][1])
    dp_min[n][1] = score[n][1] + min(dp_min[n - 1])
    dp_min[n][2] = score[n][2] + min(dp_min[n - 1][1], dp_min[n-1][2])
    dp_max[n][0] = score[n][0] + max(dp_max[n - 1][0], dp_max[n - 1][1])
    dp_max[n][1] = score[n][1] + max(dp_max[n - 1])
    dp_max[n][2] = score[n][2] + max(dp_max[n - 1][1], dp_max[n-1][2])
print(f'{max(dp_max[N - 1])} {min(dp_min[N - 1])}')