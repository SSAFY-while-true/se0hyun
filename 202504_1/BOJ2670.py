# BOJ 2670 연속부분최대곱

N = int(input())
nums = []
for _ in range(N):
    nums.append(float(input()))
# print(nums)

dp = [0] * N
dp[0] = nums[0]
for i in range(1, N):
    # print(dp[i-1] * nums[i])
    # print(nums[i])
    dp[i] = max(dp[i-1] * nums[i], nums[i])

# print(round(max(dp),3))
print('%.3f' % max(dp))