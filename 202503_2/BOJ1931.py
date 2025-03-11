# BOJ 1931 회의실 배정

import sys

input = sys.stdin.readline

def get_max_meeting_count(meetings):
    count = 0
    end_time = 0

    # 최대한 많은 회의가 목표
    for start, end in meetings:     # 끝나는 시간이 빠른 순서대로   
        if start >= end_time:       # 저장된 종료 시각보다 start가 크면 count 
            count += 1
            end_time = end

    return count

N = int(input())
meetroom_info = []
for _ in range(N):
    a, b = map(int, input().split())
    meetroom_info.append([a, b])
meetroom_info.sort(key=lambda x:(x[1], x[0]))   # 끝나는 시간 순서로 정렬

print(get_max_meeting_count(meetroom_info))

'''
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''