# 효율적인 해킹

import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)
    visited[start] = True
    count = 0

    while stack:
        v = stack.pop()
        for next_computer in computer_graph[v]:
            if not visited[next_computer]:
                visited[next_computer] = True
                stack.append(next_computer)
                count += 1
    
    return count

def make_graph(computers):
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        graph[computers[i][1]].append(computers[i][0])
        
    return graph


def hack_computers(computers):
    hacking_list = [0] * (N+1)
    global computer_graph
    computer_graph = make_graph(computers)
    for i in range(1, N+1):
        hacking_list[i] = dfs(i)
    
    max_val = max(hacking_list)
    return [index for index, val in enumerate(hacking_list) if val == max_val]


def main():
    global N, M
    N, M = map(int, input().split())
    computer_list = [list(map(int, input().split())) for _ in range(M)]
    print(*hack_computers(computer_list))

if __name__=='__main__':
    main()