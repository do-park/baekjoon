# BOJ 9465 스티커

for tc in range(int(input())):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(3)]
    dp[1][0] = sticker[0][0]
    dp[2][0] = sticker[1][0]
    for n in range(1, N):
        dp[0][n] = max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])
        dp[1][n] = sticker[0][n] + max(dp[0][n - 1], dp[2][n - 1])
        dp[2][n] = sticker[1][n] + max(dp[0][n - 1], dp[1][n - 1])
    print(max(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))