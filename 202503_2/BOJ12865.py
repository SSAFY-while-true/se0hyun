# BOJ 12865 평범한 배낭

import sys

input = sys.stdin.readline

def ordinary_bag():
    for i in range(N):
        for j in range(K, bags[i][0] - 1, -1):
            dp[j] = max(dp[j], dp[j - bags[i][0]] + bags[i][1])
    return dp[K]

N, K = map(int, input().split())
bags = []
for _ in range(N):
    W, V = map(int, input().split())
    bags.append([W, V])

dp = [0] * (K + 1)
print(ordinary_bag())