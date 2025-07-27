# BOJ 20055 컨베이어 벨트 위의 로봇

from collections import deque

N, K = map(int, input().split())
boxes = list(map(int, input().split()))

boxes = deque(boxes)
is_robot = [False] * N
is_robot = deque(is_robot)

cnt = 0

while boxes.count(0) < K:
	cnt += 1
	boxes.rotate(1)	# 컨베이어벨트 회전
	if is_robot[-1] == True:	# 내리는 위치에 로봇 존재 -> False로
		is_robot[-1] = False
	is_robot.rotate(1)	# 로봇 회전 -> 첫 번째 위치는 항상 False기 때문에 N길이를 회전시켜도 됨.
	is_robot[-1] = False
	for i in range(N-1, 0, -1):
		if boxes[i] > 0 and is_robot[i-1] == True and is_robot[i] == False:
			boxes[i] -= 1
			is_robot[i] = True
			is_robot[i-1] = False
	is_robot[-1] = False
	if boxes[0] > 0:
		is_robot[0] = True
		boxes[0] -= 1
	

print(cnt)
