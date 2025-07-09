# BOJ 1149 RGB 거리

def RGB():
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = grid[0]     # 초기값 설정
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + grid[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + grid[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + grid[i][2]
    return min(dp[N-1])

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(RGB())