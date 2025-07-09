# BOJ 14890 경사로

def is_right(target, L):
    N = len(target)
    used = [False] * N  # 경사로 설치 여부 체크
    
    for i in range(N - 1):
        if target[i] == target[i + 1]:
            continue  # 같은 높이면 통과
        
        if abs(target[i] - target[i + 1]) != 1:
            return False  # 높이 차이가 1이 아니면 불가능
        
        # 오르막길: 왼쪽에 경사로 설치
        if target[i] < target[i + 1]:
            for j in range(i - L + 1, i + 1):
                if j < 0 or used[j] or target[j] != target[i]:
                    return False
                used[j] = True
        
        # 내리막길: 오른쪽에 경사로 설치  
        else:
            for j in range(i + 1, i + L + 1):
                if j >= N or used[j] or target[j] != target[i + 1]:
                    return False
                used[j] = True
    
    return True

def get_routes():
    N, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    answer = 2 * N

    for i in range(N):
        row_target = graph[i]
        if not is_right(row_target, L):
            answer -= 1
        col_target = []
        for j in range(N):
            col_target.append(graph[j][i])
        if not is_right(col_target, L):
            answer -= 1

    return answer

if __name__=='__main__':
    print(get_routes())