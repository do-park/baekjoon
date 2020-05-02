# BOJ 15954 인형들
# 30% 부근에서 틀렸습니다.

from math import sqrt
from decimal import *

N, K = map(int, input().split())
dolls = list(map(int, input().split()))
result = Decimal('inf')
for i in range(N - K + 1):
    total = sum(dolls[i : i + K -1])
    var = sum(doll * doll for doll in dolls[i : i + K - 1])
    for j in range(K, N - i + 1):
        total += dolls[i + j - 1]
        var += dolls[i + j - 1] ** 2
        average = total / j
        standard = var / j - average ** 2
        result = min(result, standard)
print(format(sqrt(result), ".11f"))