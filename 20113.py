# 백준 20113 긴급 회의
# 120784 KB, 116 ms

N = int(input())
votes = list(map(int, input().split()))
result = [0] * (N + 1)
for vote in votes:
    result[vote] += 1
result[0] = 0
rejected = result.index(max(result))
result.sort(reverse=True)
if result[0] == result[1]:
    print('skipped')
else:
    print(rejected)