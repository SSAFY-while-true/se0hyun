# BOJ 11403 경로 찾기
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    while(queue):
        cur = queue.popleft()
        for node in range(N):
            if adj_graph[cur][node] == 1 and visited[start][node] == 0:
                visited[start][node] = 1
                queue.append(node)

N = int(input())
adj_graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    bfs(i, adj_graph)

for row in visited:
    print(*row)