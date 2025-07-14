# BOJ 10844 쉬운 계단 수

def get_stairs(N):
    dp = [0] * (N + 1)
    dp[0], dp[1], dp[2] = 0, 9, 17
    if N > 2:
        dp[N] = 2 * dp[N-1] -2
    return dp[N] % 1000000000

def main():
    N = int(input())
    print(get_stairs(N))

if __name__ == "__main__":
    main()