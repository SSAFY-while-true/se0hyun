# BOJ 2193 이친수

N = int(input())
dp = [0] * N


if N == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N-1])