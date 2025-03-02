# BOJ 1309 동물원

import sys
input = sys.stdin.readline

def make_lion_zoo(n):
    dp = [0] * (n)
    if n == 1:
        return 3
    elif n == 2:
        return 7
    
    dp[0], dp[1] = 3, 7
    
    for i in range(2, n):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901
    return dp[i]


def main():
    N = int(input())
    print(make_lion_zoo(N))


if __name__=='__main__':
    main()