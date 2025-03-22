# BOJ 10026 적록색약
from collections import deque

def bfs(grid, x, y, visited):
    flag = grid[x][y]   # 시작점 색상
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            # 시작점 색상과 같은 조건까지 검색
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == flag:
                queue.append((nx, ny))
                visited[nx][ny] = True

N = int(input())
drawing = [list(input()) for _ in range(N)]

# 평범한 사람들에게 보이는 그림
count_ord = 0
visited_ord = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited_ord[i][j] == False:
            bfs(drawing, i, j, visited_ord)
            count_ord += 1

# 적록색약에게 보이는 그림.
# R과 G를 하나의 색상으로 표현
count_rgb = 0
visited_RGB = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if drawing[i][j] == 'R':
            drawing[i][j] = 'G' 

for i in range(N):
    for j in range(N):
        if visited_RGB[i][j] == False:
            bfs(drawing, i, j, visited_RGB)
            count_rgb += 1

print(count_ord, count_rgb)