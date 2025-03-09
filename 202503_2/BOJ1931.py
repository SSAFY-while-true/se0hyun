# BOJ 1931 회의실 배정

import sys

input = sys.stdin.readline

def get_max_meeting_count(meetings):
    count = 0
    end_time = 0

    for start, end in meetings:
        if start >= end_time:
            count += 1
            end_time = end

    return count

N = int(input())
meetroom_info = []
for _ in range(N):
    a, b = map(int, input().split())
    meetroom_info.append([a, b])
meetroom_info.sort(key=lambda x:(x[1], x[0]))

print(get_max_meeting_count(meetroom_info))