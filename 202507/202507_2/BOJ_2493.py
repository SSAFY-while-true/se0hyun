# BOJ 2493 탑

N = int(input())
tops = list(map(int, input().split()))
tops.reverse()

dp = []
high = 0
answer = [0]

i = 0
while tops:
    i += 1
    cur = tops.pop()
    while dp and dp[-1][0] <= cur:
        dp.pop()
    
    if dp:
        if cur < dp[-1][0]:
            answer.append(dp[-1][1])
        elif cur < dp[high][0]:
            answer.append(dp[high][1])
        else:
            answer.append(0)
    else:
        answer.append(0)
    dp.append((cur, i))
    if cur >= dp[high][0]:
        high = len(dp) - 1  
    
print(*answer[1:])