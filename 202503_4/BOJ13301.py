# BOJ 13301 타일 장식물

N = int(input())
dp = [[0] * 2 for _ in range(N + 1)]

dp[1][0], dp[1][1] = 1, 1

for i in range(2, N + 1):
    if i % 2 == 0:
        dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][0] + dp[i-1][1]
    else:
        dp[i][0], dp[i][1] = dp[i-1][0] + dp[i-1][1], dp[i-1][1]

print(2*(dp[N][0] + dp[N][1]))