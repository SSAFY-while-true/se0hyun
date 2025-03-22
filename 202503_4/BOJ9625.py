# BOJ 9625 BABBA

K = int(input())
dp = [[0] * 2 for _ in range(K+1)]

"""
A -> B
B -> BA
BA -> BAB
BAB -> BABBA
A는 B 하나
B는 A 하나, B 하나
"""


dp[0][0], dp[0][1] = 1, 0   # a, b
for i in range(1, K+1):
    dp[i][0], dp[i][1] = dp[i-1][1], dp[i-1][0] + dp[i-1][1]

print(*dp[K])
