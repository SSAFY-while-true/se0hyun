# BOJ 2467 용액

def get_two_sol():
    start, end = 0, N-1
    sum_value = abs(solutions[start] + solutions[end])
    left, right = solutions[start], solutions[end]
    while start < end:
        temp = solutions[start] + solutions[end]
        if abs(temp) < sum_value:
            sum_value = abs(temp)
            left, right = solutions[start], solutions[end]
        if temp > 0:
            end -= 1
        elif temp < 0:
            start += 1
        else:
            return solutions[start], solutions[end]
    return left, right

N = int(input())
solutions = list(map(int, input().split()))
s, e = get_two_sol()
print(s, e)