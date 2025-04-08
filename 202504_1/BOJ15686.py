# BOJ 15686 치킨 배달
from itertools import combinations

def dfs(result, combis, homes):
    '''
    1. 0부터 M까지 치킨집 순열 생성
    2. 각 경우의 수 만큼 거리 계산
    3. 초기 result = max.inf
    4. 갱신
    5. 이미 result를 넘어가면 바로 back
    '''
    for combi in combis:
        value = 0
        if value > result:
            continue
        for home in homes:
            value += min(abs(home[0]-x)+abs(home[1]-y) for x, y in combi)
        result = min(value, result)
    
    return result

def get_positions(grid):
    chickens = []
    homes = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                chickens.append((i, j))
            elif grid[i][j] == 1:
                homes.append((i, j))
    return chickens, homes

def get_chicken_combis(chickens_position):
    combis = []
    for i in range(1, M+1):
        combis.extend(combinations(chickens_position, i))
    return combis

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
chickens, homes = get_positions(grid)
combis = get_chicken_combis(chickens)
print(dfs(result, combis, homes))