# BOJ 2644 촌수계산

import sys
from collections import deque

input = sys.stdin.readline

def make_adj_list(V, E, array):
    result_list = [[] for _ in range(V+1)]
    
    for i in range(E):
        result_list[array[i][0]].append(array[i][1])
        result_list[array[i][1]].append(array[i][0])
    
    for i in range(1, V + 1):
        result_list[i].sort()
    # print(result_list)
    return result_list

def bfs(n, m, start, target, arr):
    adj_list = make_adj_list(n, m, arr)
    visited = [0] * (n + 1)
    queue = deque([(start, 0)])

    visited[start] = 1

    while queue:
        current, distance = queue.popleft()
        if current == target:
            return distance
        
        for next_node in adj_list[current]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                queue.append([next_node, distance + 1])
    return -1

def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    arr = []
    for _ in range(m):
        arr.append(tuple(map(int, input().split())))
    result = bfs(n, m, a, b, arr)
    print(result)

if __name__ == '__main__':
    main()

'''
1
2     3
7 8 9 

4
5 6'''