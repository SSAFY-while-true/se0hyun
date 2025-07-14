# BOJ 1644 소수의 연속합

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_count(N):
    primes = []
    for i in range(2, N):
        if is_prime(i):
            primes.append(i)
    
    return primes
    
def binary_search(N):
    primes = get_count(N)
    answer = 0
    start, end = 0, len(primes) - 1
    while start <= end:
        mid = (start + end) // 2 + 1
        total = sum(primes[start:end])
        print(start, end, total)
        if total > N:
            end = mid - 1
        elif total < N:
            start = mid + 1
        else:
            print(start, end)
            answer += 1
    
    return answer
    
if __name__=="__main__":
    N = int(input())
    print(binary_search(N))
    
