# BOJ 21763 헌내기는 친구가 필요해

'''
0: 빈 공간
X: 벽
I: 도연
P: 사람
'''

import sys
from collections import deque
input = sys.stdin.readline

def find_my_position(N, M, grid):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'I':
                return (i, j)

def bfs(N, M, campus):
    count = 0
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    doyeon_x, doyeon_y = find_my_position(N, M, campus)
    queue = deque([(doyeon_x, doyeon_y)])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] == 'P':
                    count += 1
                    queue.append([nx, ny])
                    campus[nx][ny] = 'X'
                if campus[nx][ny] == 'O':
                    queue.append([nx, ny])
                    campus[nx][ny] = 'X'
    return count
    
def main():
    global N, M
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    res = bfs(N, M, grid)
    print(res if res > 0 else 'TT')


if __name__=='__main__':
    main()
