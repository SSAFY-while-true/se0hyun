# Programmers 389479 서버 증설 횟수

from collections import deque
def solution(players, m, k):
    queue = deque()
    answer = 0
    for player in players:  
        if queue:
            queue = deque(x - 1 for x in queue) # 1시간 지남 -> 서버 사용시간 줄어듬
        while queue:
            if queue[0] == 0:   # 사용 완료 서버 종료
                queue.popleft()
            else:
                break
        if player >= (len(queue) + 1) * m:  # 한 대는 기본적으로 있음 => +1
            for _ in range((player - (len(queue) + 1) * m) // m + 1):   # 필요 서버 개수만큼 서버 추가
                queue.append(k)
                answer += 1
    return answer