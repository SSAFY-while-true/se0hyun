from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[0] * m for _ in range(n)]   # visited 초기화
    cols_oil = [0] * m
    
    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = 1
        cols = set([c])
        result = 1      # 이미 시작점 +1
        
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    result += 1
                    cols.add(ny)
        for col in cols:
            cols_oil[col] += result
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:  # 석유가 있음
                bfs(i, j)    # bfs에 넣고
    return max(cols_oil)