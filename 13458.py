# BOJ 13458 시험 감독

from math import ceil


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = N
for students in A:
    if students > B:
        answer += ceil((students - B) / C)
print(answer)