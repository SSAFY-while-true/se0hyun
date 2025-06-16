# BOJ 2166 다각형의 면적

N = int(input())

x_list, y_list = [], []

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x), y_list.append(y)
    
x_sum, y_sum = 0, 0

for i in range(N):
    j = (i + 1) % N
    x_sum += x_list[i] * y_list[j]
    y_sum += y_list[i] * x_list[j]

print(round(abs(x_sum - y_sum) /2, 1))
