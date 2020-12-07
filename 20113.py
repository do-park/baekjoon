# 백준 20113 긴급 회의
# 120784 KB, 116 ms

N = int(input())
votes = list(map(int, input().split()))
result = [0] * (N + 1)
for vote in votes:
    if vote != 0:
        result[vote] += 1
rejected = result.index(max(result))
result.sort(reverse=True)
if result[0] == result[1]:
    print('skipped')
else:
    print(rejected)