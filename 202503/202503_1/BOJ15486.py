# BOJ 15486 퇴사 2

import sys
input = sys.stdin.readline

def make_max_profit(n, work_table):
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i])
        end_date = i + work_table[i][0]
        if end_date <= n:
            dp[end_date] = max(dp[end_date], dp[i] + work_table[i][1])
        

    return dp[n]

def main():
    N = int(input())
    work_list = [list(map(int, input().split())) for _ in range(N)]
    print(make_max_profit(N, work_list))

if __name__=='__main__':
    main()