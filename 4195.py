# BOJ 4195 친구 네트워크

import sys

def find_set(x):
    if type(friends[x]) is int:
        return x
    friends[x] = find_set(friends[x])
    return friends[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        friends[x] += friends[y]
        friends[y] = x
    else:
        friends[y] += friends[x]
        friends[x] = y
    return


for tc in range(1, int(sys.stdin.readline().rstrip())+ 1):
    friends = dict()
    F = int(sys.stdin.readline().rstrip())
    for f in range(F):
        A, B = sys.stdin.readline().split()
        if not friends.get(A):
            friends[A] = -1
        if not friends.get(B):
            friends[B] = -1
        union(A, B)
        print(abs(friends[find_set(B)]))