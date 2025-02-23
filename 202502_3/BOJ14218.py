# BOJ 14218 그래프 탐색 2

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, target, adj_list):
    n = len(adj_list)
    # print(target)
    queue = deque([(start, 0)])
    # print(queue)
    visited = [False for _ in range(n)]
    while queue:
        current, distance = queue.popleft()
        # print(current)
        if current == target:
            return distance
        for next_node in adj_list[current]:
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append([next_node, distance + 1])
    return -1


def make_city(n, array, city1, city2):
    result = [0 for _ in range(n)]
    array[city1].append(city2)
    array[city2].append(city1)
    # print(array)
    for i in range(1, n+1):
        array[i].sort()
        result[i - 1] = bfs(1, i, array)
    
    return result


def main():
    n, m = map(int, input().split())
    roads = [[] for _ in range(n+1)]
    # print(roads)
    for _ in range(m):
        i, j = map(int, input().split())
        roads[i].append(j)
        roads[j].append(i)
    q = int(input())
    for _ in range(q):
        i, j = map(int, input().split())
        # roads[i].append(j)
        # roads[j].append(i)
        print(*make_city(n, roads, i, j))


if __name__ == '__main__':
    main()