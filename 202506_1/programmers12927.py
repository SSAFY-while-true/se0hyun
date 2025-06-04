import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    max_heap = [-x for x in works]
    heapq.heapify(max_heap)
    for _ in range(n):
        max_value = -heapq.heappop(max_heap)  # 최댓값 꺼내기
        max_value -= 1                        # 작업량 줄이기
        heapq.heappush(max_heap, -max_value)
    
    answer = sum(map(lambda x: x * x, max_heap))
    return answer