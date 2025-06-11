# BOJ 1058 친구
import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
dist = [[0] * (N) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                dist[i][j] = 1

answer = 0
for row in dist:
    answer = max(answer, row.count(1))
print(answer)