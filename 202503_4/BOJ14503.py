# BOJ 14503 로봇 청소기
# from collections import deque
import sys
input = sys.stdin.readline

def dfs(start, end, dir):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 북 동 남 서
    stack = [(start, end, dir)]
    result = 1

    while stack:
        cx, cy, cd = stack.pop()
        for i in range(4):
            nd = (cd + 3 - i) % 4
            dx, dy = dirs[nd]
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    stack.append((nx, ny, nd))
                    visited[nx][ny] = True
                    result += 1
                    break
                
        else:
            opp_dir = (cd + 2) % 4     # 현재 반대 방향
            opp_x, opp_y = dirs[opp_dir]
            bx, by = cx + opp_x, cy + opp_y
            if 0 <= bx < N and 0 <= by < M and grid[bx][by] == 0:
                stack.append((bx, by, cd))
            else:
                return result

    return result

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            visited[i][j] = True
visited[r][c] = True
print(dfs(r, c, d))