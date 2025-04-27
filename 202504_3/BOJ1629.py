# BOJ 1629 곱셈

A, B, C = map(int, input().split())
remain = 0
mul = A
for _ in range(B-1):
    mul = mul * A
    remain += mul % C
    if remain >= C:
        remain -= C
print(remain)