# BOJ 7662 이중 우선순위 큐
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    count = defaultdict(int)

    for _ in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(min_h, val)
            heapq.heappush(max_h, -val)
            count[val] += 1
        else:
            if val == 1:
                while max_h:
                    max_val = -heapq.heappop(max_h)
                    if count[max_val] > 0:
                        count[max_val] -= 1
                        break
            else:
                while min_h:
                    min_val = heapq.heappop(min_h)
                    if count[min_val] > 0:
                        count[min_val] -= 1
                        break

    # 유효한 최대/최소 찾기
    max_val, min_val = None, None
    while max_h:
        v = -heapq.heappop(max_h)
        if count[v] > 0:
            max_val = v
            break
    while min_h:
        v = heapq.heappop(min_h)
        if count[v] > 0:
            min_val = v
            break

    if max_val is None or min_val is None:
        print('EMPTY')
    else:
        print(max_val, min_val)
