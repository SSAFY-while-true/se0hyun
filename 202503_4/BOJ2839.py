# BOJ 2839 설탕 배달

N = int(input())

max_val = N // 3
min_val = N // 5 

result = max_val + 1
for cnt in range(min_val, max_val + 1):
    for i in range(cnt + 1):
        three = i
        five = cnt - i
        if three * 3 + five * 5 == N:
            result = min(cnt, result)

print(-1) if result == max_val + 1 else print(result)

"""
나올 수 있는 설탕 봉지 최대/최소값
ex) 6개의 봉지를 사용한다면
0-6까지 돌면서 3kg/5kg으로 나눔
각 무게와 곱한 값이 N과 같다면 값 갱신
"""
