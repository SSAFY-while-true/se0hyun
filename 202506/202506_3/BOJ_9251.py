# BOJ 9251 LCS
from itertools import combinations
import sys

input = sys.stdin.readline

fir_str, sec_str = list(input().split()), list(input().split())

answer = 0

for i in range(len(fir_str)):
    current = fir_str[i]
    for j in range(len(sec_str)):
        if current != sec_str[j]:
            continue
        else:
            break

# fir_com, sec_com = set(), set()

# fir_com = set(element for i in range(1, len(fir_str)) for element in combinations(fir_str, i))
# sec_com = set(element for i in range(1, len(sec_str)) for element in combinations(sec_str, i))

# answer = 0
# for com in fir_com:
#     if com in sec_com:
#         # print(com)
#         answer = max(answer, len(com))

print(answer - 1)

'''
AC
AP'''