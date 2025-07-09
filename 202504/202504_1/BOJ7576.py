# BOJ 7576 토마토
import sys
from collections import deque

input = sys.stdin.readline

def get_tomato(grid):
    tomatos = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                tomatos.append((i, j, 0))
    return tomatos

def bfs(tomatos):
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]
    queue = deque(tomatos)
    day = 0

    while queue:
        cx, cy, day = queue.popleft()
        # print(cx, cy)
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] == 0:
                    queue.append((nx, ny, day+1))
                    grid[nx][ny] = 1
    for row in grid:
        if 0 in row:
            return -1
    return day

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
tomatos = get_tomato(grid)
print(bfs(tomatos))