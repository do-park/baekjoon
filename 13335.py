# BOJ 13335 트럭

from collections import deque
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque()
weight = 0
turn_i = 0
turn_o = 0
time = 1
while True:
    for i in range(len(bridge)):
        bridge[i] += 1
    if bridge and bridge[0] > W:
        bridge.popleft()
        weight -= trucks[turn_o]
        turn_o += 1
    if len(bridge) < W and weight + trucks[turn_i] <= L:
        bridge.append(1)
        weight += trucks[turn_i]
        turn_i += 1
    if turn_i == N:
        time += W
        break
    time += 1
print(time)