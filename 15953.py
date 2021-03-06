# BOJ 15953 상금 헌터

cf2017 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50,
          30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
cf2018 = [0, 512, 256, 256, 128, 128, 128, 128,
          64, 64, 64, 64, 64, 64, 64, 64,
          32, 32, 32, 32, 32, 32, 32, 32,
          32, 32, 32, 32, 32, 32, 32, 32]

for tc in range(int(input())):
    grade7, grade8 = map(int, input().split())
    money = 0
    if grade7 < 22:
        money += cf2017[grade7]
    if grade8 < 32:
        money += cf2018[grade8]
    print(money * 10000)